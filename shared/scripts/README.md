---
last_updated: 2026-04-26
version: 1.1.0
file_status: protocol
---

# Shared Scripts

This directory contains executable scripts that can be used across multiple projects.

## Available Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| workcap_analyzer.py | Analyze workspace and validate cross-references | `python workcap_analyzer.py` |
| fix_filenames.py | Rename files to follow naming conventions | `python fix_filenames.py` |

## Additional Scripts (`scripts/`)

The following scripts live in `scripts/` and are available for use:

| Script | Purpose | Usage |
|--------|---------|-------|
| scripts/office_unzip.py | Extract, inspect, standardize, and repack Office Open XML files (.xlsx, .xlsm, .docx, .pptx) | See below |
| scripts/metadata_wizard.py | Interactive YAML frontmatter manager for markdown files | `python scripts/metadata_wizard.py` |

### office_unzip.py — KABDMSV2 Office File Utilities

Handles all Office Open XML formats (`.xlsx`, `.xlsm`, `.docx`, `.docm`, `.pptx`, `.pptm`, etc.).

```bash
# Inspect properties and ZIP structure
python scripts/office_unzip.py inspect <file>

# Extract to directory for XML editing
python scripts/office_unzip.py extract <file> [output_dir]

# Apply KABDMSV2 standard properties in-place (auto-backup created)
#   creator → KAB
#   lastModifiedBy → Kyle Breneman
#   Company → KABDMSV2
#   modified → current UTC timestamp
python scripts/office_unzip.py standardize <file>
python scripts/office_unzip.py standardize <file> --no-backup

# Repack an edited extracted directory back into an Office file
python scripts/office_unzip.py repack <extracted_dir> <output_file>
```

## Adding New Scripts

1. Place the script file in this directory
2. Update this README with usage information
3. Ensure the script uses relative paths for any data file references

[See: ../README.md for shared resources overview]
