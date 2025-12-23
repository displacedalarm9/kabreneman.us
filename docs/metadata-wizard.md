---
last_updated: 2025-12-19
version: 1.0.0
file_status: documentation
---

# Metadata Wizard Guide

## Overview

The Metadata Wizard is an interactive command-line tool for creating and managing YAML frontmatter metadata in markdown files. It supports two modes:

1. **Simple Mode**: Basic markdown frontmatter (last_updated, version, file_status)
2. **DOCSYS Mode**: Full provenance tracking with DOCSYS/UNISYS integration

## Features

### Simple Mode
- Last updated date (YYYY-MM-DD)
- Version number (SemVer format)
- File status (template, protocol, active, report, archive)
- Custom fields

### DOCSYS Mode
- **System tracking**: WORKCAP, UNISYS, DOCSYS, REDOREPO, NDS, FINTRACK
- **Cycle alignment**: Year 1, Year 2, Continuous, etc.
- **Provenance fields**:
  - TSN (Trace Sequence Number) - auto-generated unique identifier
  - Date (ISO-8601 format)
  - Version (SemVer format)
- **Artifact taxonomy**:
  - Artifact types: ProjectSupport, Finance, Legal, Medical, etc.
  - Subtypes: ActivityLedger, ConversationLog, Invoice, etc.
- **Retention classes**: preserved, versioned, consolidated, archived, deleted
- **Cross-references**: GitHub issues, OneDrive IDs, REDOREPO references
- **Governance**: Sensitive data flags, .gitignore enforcement, encryption
- **Footer stamp**: Auto-generated provenance stamp for printouts

## Installation

No installation required. The wizard is located at:
```
scripts/metadata_wizard.py
```

### Prerequisites
- Python 3.7+
- PyYAML library (install with `pip install pyyaml`)

## Usage

### Basic Usage

```bash
python scripts/metadata_wizard.py
```

The wizard will guide you through an interactive session:

1. Select mode (Simple or DOCSYS)
2. Enter file path (existing or new file)
3. Fill in metadata fields
4. Preview metadata
5. Optionally export to separate files (YAML, TXT, MD)
6. Save to file

### Example: Simple Mode

```bash
$ python scripts/metadata_wizard.py
======================================================================
METADATA WIZARD - DOCSYS/UNISYS Integration
======================================================================

Select metadata mode:
  1. Simple (markdown frontmatter only)
  2. DOCSYS (full provenance tracking with TSN, cycles, etc.)

Mode [1/2]: 1

Enter the file path (relative or absolute): templates/new_template.md
File does not exist. Create it? (y/n): y

Last updated date [2025-12-19] (YYYY-MM-DD): 
Version [1.0.0]: 
File status [template]: 

Add custom fields? (y/n): n

======================================================================
METADATA PREVIEW
======================================================================

---
last_updated: 2025-12-19
version: 1.0.0
file_status: template
---

Proceed with save? (y/n): y
✓ File saved: /path/to/templates/new_template.md
✓ Metadata wizard completed successfully!
```

### Example: DOCSYS Mode

```bash
$ python scripts/metadata_wizard.py

Select metadata mode:
  1. Simple (markdown frontmatter only)
  2. DOCSYS (full provenance tracking with TSN, cycles, etc.)

Mode [1/2]: 2

Enter the file path: docs/workcap_artifact.md

Available systems: WORKCAP, UNISYS, DOCSYS, REDOREPO, NDS, FINTRACK
System [UNISYS]: WORKCAP

Cycle (e.g., 'Year 1', 'Year 2', 'Continuous') [Continuous]: Year 1

Artifact types: ProjectSupport, Finance, Legal, Medical, ...
Artifact type [ProjectSupport]: Finance

Subtypes for Finance: Invoice, UtilityBill, Statement, Report
Subtype(s) (comma-separated): Invoice, UtilityBill

TSN [20251219-A5FA] (auto-generated): 
Date (ISO-8601) [2025-12-19]: 
Version (SemVer) [v1.0.0]: 

Source (e.g., 'Evergy', 'Copilot'): Evergy

Purpose (one per line, empty line to finish):
  - Track utility billing for WORKCAP cycle
  - Provide financial audit trail
  - 

Filing path: /WORKCAP/FIN/UTILITY/2025-12_Evergy.pdf

Retention classes: preserved, versioned, consolidated, archived, deleted
Retention class [preserved]: 

GitHub issue numbers (comma-separated): 33, 39
OneDrive file IDs (comma-separated): 
REDOREPO references (comma-separated): WORKCAP-UTILITY-2025

Contains sensitive data? (y/n) [n]: n
Enforce .gitignore? (y/n) [y]: y
Encryption required? (y/n) [n]: n

Narrative context (multi-line, Ctrl+D or Ctrl+Z to finish):
This invoice is part of the WORKCAP Year 1 financial restoration cycle.
^D

======================================================================
METADATA PREVIEW
======================================================================

---
system: WORKCAP
cycle: Year 1
artifact_type: Finance
subtype:
- Invoice
- UtilityBill
provenance:
  tsn: 20251219-A5FA
  date: '2025-12-19'
  version: v1.0.0
artifact_metadata:
  source: Evergy
  purpose:
  - Track utility billing for WORKCAP cycle
  - Provide financial audit trail
  filing_path: /WORKCAP/FIN/UTILITY/2025-12_Evergy.pdf
  retention_class: preserved
cross_references:
  github_issues:
  - 33
  - 39
  redorepo_refs:
  - WORKCAP-UTILITY-2025
governance:
  sensitive_data: false
  gitignore_enforced: true
  encryption_required: false
footer_stamp: DOCSYS | WORKCAP | Finance | TSN:20251219-A5FA
narrative_context: |
  This invoice is part of the WORKCAP Year 1 financial restoration cycle.
---

======================================================================
FOOTER STAMP
======================================================================

DOCSYS | WORKCAP | Finance | TSN:20251219-A5FA

Export metadata to separate files (YAML/TXT/MD)? (y/n): y
✓ YAML metadata exported: /path/to/docs/workcap_artifact_metadata.yaml
✓ Plain text metadata exported: /path/to/docs/workcap_artifact_metadata.txt
✓ Markdown overlay exported: /path/to/docs/workcap_artifact_metadata.md

Proceed with save? (y/n): y
✓ File saved: /path/to/docs/workcap_artifact.md
✓ Metadata wizard completed successfully!
```

## Export Formats

When you choose to export metadata to separate files, the wizard creates:

### 1. YAML Export (.yaml)
Complete YAML representation of all metadata fields, suitable for programmatic processing.

### 2. Plain Text Export (.txt)
Human-readable summary of key metadata fields:
- System, Cycle, Artifact Type
- TSN, Date, Version
- Footer stamp

### 3. Markdown Overlay (.md)
DOCSYS intake overlay in markdown format, ready to be copied/pasted onto PDF documents:
- Formatted as a visual overlay
- Includes all key provenance fields
- Shows footer stamp for printouts

## Metadata Fields Reference

### Simple Mode Fields

| Field | Description | Format | Example |
|-------|-------------|--------|---------|
| last_updated | Last modification date | YYYY-MM-DD | 2025-12-19 |
| version | Document version | SemVer | 1.0.0 |
| file_status | Document status | Enum | template, protocol, active, report, archive |

### DOCSYS Mode Fields

| Field | Description | Format | Example |
|-------|-------------|--------|---------|
| system | Top-level system | String | WORKCAP, UNISYS, DOCSYS |
| cycle | Cycle identifier | String | Year 1, Year 2, Continuous |
| artifact_type | Type classification | Enum | ProjectSupport, Finance, Legal |
| subtype | Sub-classification | List | [Invoice, UtilityBill] |
| provenance.tsn | Trace Sequence Number | YYYYMMDD-XXXX | 20251219-A5FA |
| provenance.date | Creation date | ISO-8601 | 2025-12-19 |
| provenance.version | Version | SemVer with 'v' prefix | v1.0.0 |
| artifact_metadata.source | Origin source | String | Evergy, Copilot |
| artifact_metadata.purpose | Purpose list | List | [Track billing, Audit trail] |
| artifact_metadata.filing_path | Storage path | Path | /WORKCAP/FIN/UTILITY/... |
| artifact_metadata.retention_class | Retention policy | Enum | preserved, versioned, archived |
| cross_references.github_issues | Related issues | List of integers | [33, 39] |
| cross_references.onedrive_ids | OneDrive file IDs | List | [file-id-123] |
| cross_references.redorepo_refs | REDOREPO references | List | [WORKCAP-UTILITY-2025] |
| governance.sensitive_data | Contains PII | Boolean | true, false |
| governance.gitignore_enforced | Enforce .gitignore | Boolean | true, false |
| governance.encryption_required | Needs encryption | Boolean | true, false |
| footer_stamp | Provenance stamp | Generated | DOCSYS \| WORKCAP \| Finance \| TSN:... |
| narrative_context | Human context | Multi-line text | Explanation of purpose |

## Best Practices

### For Simple Mode
1. Always use ISO-8601 date format (YYYY-MM-DD)
2. Follow SemVer for version numbers
3. Use appropriate file_status values
4. Update last_updated when making significant changes

### For DOCSYS Mode
1. **System Selection**: Choose the appropriate top-level system
2. **Cycle Tracking**: Align with your project cycles (Year 1, Year 2, etc.)
3. **TSN Management**: Keep auto-generated TSNs; they ensure uniqueness
4. **Filing Paths**: Use consistent path structures within your systems
5. **Cross-References**: Link related artifacts for traceability
6. **Narrative Context**: Provide meaningful explanations for future reference
7. **Footer Stamps**: Use on all printouts for provenance tracking

### General Tips
- Run the wizard when creating new documents
- Update metadata when making significant changes
- Export to separate files for archival purposes
- Use the preview feature to verify before saving
- Keep existing files when updating (wizard preserves content)

## Integration with Repository

The Metadata Wizard integrates with the kabreneman.us repository structure:

- **Templates**: `/templates/` - Use simple mode for template files
- **Documentation**: `/docs/` - Use either mode based on needs
- **WORKCAP Artifacts**: Use DOCSYS mode with WORKCAP system
- **Configuration**: `/configs/` - Use simple mode with custom fields

## Troubleshooting

### Common Issues

**Issue**: "Error: File path cannot be empty"
- **Solution**: Always provide a valid file path when prompted

**Issue**: "ModuleNotFoundError: No module named 'yaml'"
- **Solution**: Install PyYAML: `pip install pyyaml`

**Issue**: "Error: Invalid file status"
- **Solution**: Use one of: template, protocol, active, report, archive

**Issue**: Multi-line input doesn't work
- **Solution**: Press Ctrl+D (Unix/Mac) or Ctrl+Z+Enter (Windows) to finish

### Getting Help

- Check this documentation
- Review examples in existing repository files
- See [docs/filename.md](filename.md) for naming conventions
- See [docs/report-standards.md](report-standards.md) for metadata standards

## See Also

- [File Naming Conventions](filename.md)
- [Report Generation Standards](report-standards.md)
- [WORKCAP Analyzer](../scripts/workcap_analyzer.py)
- [Repository README](../README.md)
