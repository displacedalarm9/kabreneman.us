#!/usr/bin/env python3
"""
Office File Utilities - KABDMSV2

Extract, inspect, standardize, and repack Office Open XML files
(.xlsx, .xlsm, .docx, .docm, .pptx, .pptm) for the KABDMSV2 document system.

Operations:
    extract     Unzip an Office file to a directory for XML inspection or editing
    inspect     Display key properties and full ZIP structure
    standardize Apply KABDMSV2 standard core properties in-place (auto-backup)
    repack      Recreate an Office file from a previously-extracted directory

Usage:
    python scripts/office_unzip.py extract <file> [output_dir]
    python scripts/office_unzip.py inspect <file>
    python scripts/office_unzip.py standardize <file> [--no-backup]
    python scripts/office_unzip.py repack <extracted_dir> <output_file>
"""

import argparse
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

# ── KABDMSV2 Standards ───────────────────────────────────────────────────────

KABDMSV2_CREATOR = "KAB"
KABDMSV2_AUTHOR = "Kyle Breneman"
KABDMSV2_COMPANY = "KABDMSV2"

# ── XML namespace map ────────────────────────────────────────────────────────

_NS = {
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "ap": "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties",
    "vt": "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes",
}

# Supported Office Open XML extensions
_OFFICE_EXTENSIONS = {
    ".xlsx", ".xlsm", ".xltx", ".xltm",
    ".docx", ".docm", ".dotx", ".dotm",
    ".pptx", ".pptm", ".potx", ".potm",
}


def _register_namespaces() -> None:
    """Register all known namespaces so ET preserves prefixes on round-trip."""
    for prefix, uri in _NS.items():
        ET.register_namespace(prefix, uri)
    # Default namespace used by app.xml
    ET.register_namespace(
        "",
        "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties",
    )


def _file_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".xlsx", ".xlsm", ".xltx", ".xltm"}:
        return "Excel"
    if ext in {".docx", ".docm", ".dotx", ".dotm"}:
        return "Word"
    if ext in {".pptx", ".pptm", ".potx", ".potm"}:
        return "PowerPoint"
    return "Unknown"


def _require_office_file(path: Path) -> None:
    if path.suffix.lower() not in _OFFICE_EXTENSIONS:
        raise ValueError(f"Not a supported Office file: {path}")
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── extract ──────────────────────────────────────────────────────────────────

def extract(file_path: Path, output_dir: Path = None) -> Path:
    """Unzip an Office file to *output_dir* (default: <stem>_extracted/)."""
    _require_office_file(file_path)

    if output_dir is None:
        output_dir = file_path.parent / f"{file_path.stem}_extracted"

    if output_dir.exists():
        print(f"[WARN] Output directory exists — existing files will be overwritten: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(file_path, "r") as zf:
        zf.extractall(output_dir)
        count = len(zf.namelist())

    print(f"[OK] Extracted {count} entries to: {output_dir}")
    return output_dir


# ── inspect ──────────────────────────────────────────────────────────────────

def inspect(file_path: Path) -> None:
    """Print core properties, app properties, and ZIP contents."""
    _require_office_file(file_path)

    ftype = _file_type(file_path)
    size_kb = file_path.stat().st_size / 1024

    print(f"\n{'='*60}")
    print(f"  {file_path.name}")
    print(f"{'='*60}")
    print(f"  Type  : {ftype} ({file_path.suffix})")
    print(f"  Size  : {size_kb:.1f} KB")

    with zipfile.ZipFile(file_path, "r") as zf:
        names = zf.namelist()
        print(f"  Parts : {len(names)} ZIP entries\n")

        if "docProps/core.xml" in names:
            _print_core_props(zf.read("docProps/core.xml"))

        if "docProps/app.xml" in names:
            _print_app_props(zf.read("docProps/app.xml"), ftype)

        print(f"\n  {'─'*56}")
        print("  ZIP Contents:")
        for name in sorted(names):
            info = zf.getinfo(name)
            print(f"    {name:<58} {info.file_size:>8} B")

    print()


def _print_core_props(xml_bytes: bytes) -> None:
    _register_namespaces()
    root = ET.fromstring(xml_bytes)

    def _text(tag_uri, tag_local):
        return root.findtext(f"{{{tag_uri}}}{tag_local}") or "—"

    print("  Core Properties:")
    print(f"    Creator          : {_text(_NS['dc'], 'creator')}")
    print(f"    Last Modified By : {_text(_NS['cp'], 'lastModifiedBy')}")
    print(f"    Created          : {_text(_NS['dcterms'], 'created')}")
    print(f"    Modified         : {_text(_NS['dcterms'], 'modified')}")

    for tag in ("title", "description", "subject", "keywords"):
        val = _text(_NS["dc"], tag)
        if val != "—":
            print(f"    {tag.capitalize():<17}: {val}")


def _print_app_props(xml_bytes: bytes, ftype: str) -> None:
    _register_namespaces()
    root = ET.fromstring(xml_bytes)
    ap, vt = _NS["ap"], _NS["vt"]

    def _find(tag):
        return (
            root.findtext(f"{{{ap}}}{tag}")
            or root.findtext(tag)
            or "—"
        )

    print("\n  Application Properties:")
    print(f"    Application : {_find('Application')}")
    print(f"    Version     : {_find('AppVersion')}")

    company = _find("Company")
    if company != "—":
        print(f"    Company     : {company}")

    if ftype == "Excel":
        titles_el = root.find(f"{{{ap}}}TitlesOfParts")
        if titles_el is None:
            titles_el = root.find("TitlesOfParts")
        if titles_el is not None:
            vec = titles_el.find(f"{{{vt}}}vector")
            if vec is not None:
                sheets = [el.text for el in vec.findall(f"{{{vt}}}lpstr")]
                preview = ", ".join(sheets[:5])
                suffix = " …" if len(sheets) > 5 else ""
                print(f"    Sheets ({len(sheets)})  : {preview}{suffix}")

    elif ftype == "Word":
        for field in ("Pages", "Words", "Characters"):
            val = _find(field)
            if val != "—":
                print(f"    {field:<12}: {val}")

    elif ftype == "PowerPoint":
        slides = _find("Slides")
        if slides != "—":
            print(f"    Slides      : {slides}")


# ── standardize ──────────────────────────────────────────────────────────────

def standardize(file_path: Path, backup: bool = True) -> None:
    """Apply KABDMSV2 standard properties to an Office file in-place."""
    _require_office_file(file_path)

    if backup:
        backup_path = file_path.with_name(file_path.stem + "_bak" + file_path.suffix)
        shutil.copy2(file_path, backup_path)
        print(f"[OK] Backup created : {backup_path}")

    # Read every ZIP entry into memory
    entries: dict[str, bytes] = {}
    with zipfile.ZipFile(file_path, "r") as zf:
        for name in zf.namelist():
            entries[name] = zf.read(name)

    # Patch or create docProps/core.xml
    if "docProps/core.xml" in entries:
        entries["docProps/core.xml"] = _patch_core_xml(entries["docProps/core.xml"])
    else:
        entries["docProps/core.xml"] = _create_core_xml()
        # Register in [Content_Types].xml if present
        if "[Content_Types].xml" in entries:
            entries["[Content_Types].xml"] = _register_core_content_type(
                entries["[Content_Types].xml"]
            )
    print("[OK] Patched         : docProps/core.xml")

    # Patch docProps/app.xml (set Company field)
    if "docProps/app.xml" in entries:
        entries["docProps/app.xml"] = _patch_app_xml(entries["docProps/app.xml"])
        print("[OK] Patched         : docProps/app.xml")

    # Write the modified ZIP back to the original path
    _write_zip(file_path, entries)
    print(f"[OK] Standardized    : {file_path}")


def _patch_core_xml(xml_bytes: bytes) -> bytes:
    """Set creator, lastModifiedBy, and modified date to KABDMSV2 standards."""
    _register_namespaces()
    root = ET.fromstring(xml_bytes)
    cp, dc, dcterms, xsi = _NS["cp"], _NS["dc"], _NS["dcterms"], _NS["xsi"]

    def _set(parent, ns, local, text, extra_attrib=None):
        el = parent.find(f"{{{ns}}}{local}")
        if el is None:
            el = ET.SubElement(parent, f"{{{ns}}}{local}")
            if extra_attrib:
                for k, v in extra_attrib.items():
                    el.set(k, v)
        el.text = text

    _set(root, dc, "creator", KABDMSV2_CREATOR)
    _set(root, cp, "lastModifiedBy", KABDMSV2_AUTHOR)
    _set(
        root,
        dcterms,
        "modified",
        _utc_now(),
        extra_attrib={f"{{{xsi}}}type": "dcterms:W3CDTF"},
    )

    return ET.tostring(root, encoding="UTF-8", xml_declaration=True)


def _create_core_xml() -> bytes:
    """Build a minimal docProps/core.xml with KABDMSV2 defaults."""
    now = _utc_now()
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        "<cp:coreProperties"
        ' xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"'
        ' xmlns:dc="http://purl.org/dc/elements/1.1/"'
        ' xmlns:dcterms="http://purl.org/dc/terms/"'
        ' xmlns:dcmitype="http://purl.org/dc/dcmitype/"'
        ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f"<dc:creator>{KABDMSV2_CREATOR}</dc:creator>"
        f"<cp:lastModifiedBy>{KABDMSV2_AUTHOR}</cp:lastModifiedBy>"
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>'
        "</cp:coreProperties>"
    ).encode("UTF-8")


def _register_core_content_type(xml_bytes: bytes) -> bytes:
    """Add the core-properties Override entry to [Content_Types].xml if missing."""
    _register_namespaces()
    ET.register_namespace(
        "", "http://schemas.openxmlformats.org/package/2006/content-types"
    )
    root = ET.fromstring(xml_bytes)
    ct_ns = "http://schemas.openxmlformats.org/package/2006/content-types"
    core_ct = (
        "application/vnd.openxmlformats-package.core-properties+xml"
    )
    # Check if already registered
    for override in root.findall(f"{{{ct_ns}}}Override"):
        if override.get("PartName") == "/docProps/core.xml":
            return xml_bytes
    ET.SubElement(
        root,
        f"{{{ct_ns}}}Override",
        PartName="/docProps/core.xml",
        ContentType=core_ct,
    )
    return ET.tostring(root, encoding="UTF-8", xml_declaration=True)


def _patch_app_xml(xml_bytes: bytes) -> bytes:
    """Set Company field in docProps/app.xml to KABDMSV2."""
    _register_namespaces()
    root = ET.fromstring(xml_bytes)
    ap = _NS["ap"]

    company_el = root.find(f"{{{ap}}}Company")
    if company_el is None:
        company_el = root.find("Company")
    if company_el is None:
        company_el = ET.SubElement(root, f"{{{ap}}}Company")
    company_el.text = KABDMSV2_COMPANY

    return ET.tostring(root, encoding="UTF-8", xml_declaration=True)


def _write_zip(file_path: Path, entries: dict) -> None:
    """Atomically replace *file_path* with a new ZIP built from *entries*."""
    tmp_path = file_path.with_name(file_path.stem + "_tmp" + file_path.suffix)
    try:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for name, data in entries.items():
                zf.writestr(name, data)
        tmp_path.replace(file_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


# ── repack ───────────────────────────────────────────────────────────────────

def repack(extracted_dir: Path, output_file: Path) -> None:
    """Recreate an Office file from a previously-extracted directory."""
    if not extracted_dir.is_dir():
        raise FileNotFoundError(f"Directory not found: {extracted_dir}")

    if output_file.exists():
        print(f"[WARN] Output file exists and will be overwritten: {output_file}")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        count = 0
        for entry in sorted(extracted_dir.rglob("*")):
            if entry.is_file():
                arcname = entry.relative_to(extracted_dir).as_posix()
                zf.write(entry, arcname)
                count += 1

    print(f"[OK] Repacked {count} files to: {output_file}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="office_unzip.py",
        description="Office File Utilities for KABDMSV2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/office_unzip.py inspect OPERCAP1.xlsm\n"
            "  python scripts/office_unzip.py extract OPERCAP1.xlsm\n"
            "  python scripts/office_unzip.py standardize OPERCAP1.xlsm\n"
            "  python scripts/office_unzip.py repack OPERCAP1_extracted/ OPERCAP1_new.xlsm\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("extract", help="Unzip Office file to directory")
    p.add_argument("file", type=Path, help="Office file (.xlsx, .docx, etc.)")
    p.add_argument(
        "output_dir",
        type=Path,
        nargs="?",
        help="Output directory (default: <file>_extracted/)",
    )

    p = sub.add_parser("inspect", help="Print properties and ZIP structure")
    p.add_argument("file", type=Path, help="Office file to inspect")

    p = sub.add_parser(
        "standardize",
        help="Apply KABDMSV2 standard properties in-place",
    )
    p.add_argument("file", type=Path, help="Office file to standardize")
    p.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip creating a backup copy before modifying",
    )

    p = sub.add_parser("repack", help="Recreate Office file from extracted directory")
    p.add_argument("extracted_dir", type=Path, help="Extracted Office XML directory")
    p.add_argument("output_file", type=Path, help="Output Office file path")

    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    try:
        if args.command == "extract":
            extract(args.file, args.output_dir)
        elif args.command == "inspect":
            inspect(args.file)
        elif args.command == "standardize":
            standardize(args.file, backup=not args.no_backup)
        elif args.command == "repack":
            repack(args.extracted_dir, args.output_file)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
