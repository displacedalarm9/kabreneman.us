---
last_updated: 2025-06-06
version: 1.0.0
file_status: log  # Changed from protocol to log
---

# Archive Protocol

[See: standards.md for file status definitions]

## Structure
/archive/
  /deleted/    # Removed files
    /{year}/   # By removal year
      /Q{1-4}/ # By quarter
  /versions/   # Previous versions
    /{year}/   # By year
      /Q{1-4}/ # By quarter

## Deleted Files
| Original File | Archived Location | Removal Date | Notes |
|--------------|------------------|--------------|-------|
| opercap1.md | deleted/2024/Q1/opercap1.md | 2024-01-18 | Merged into templates |
| reports.md | deleted/2024/Q1/reports.md | 2024-01-18 | Merged into standards |
| folder-audit.md | deleted/2024/Q1/folder-audit.md | 2024-01-18 | Split into standards |

## Version History
| System | Version | Location | Date | Notes |
|--------|---------|----------|------|-------|
| OPERCAP | 1.0.0 | 2025/Q2/templates/opercap1.md | 2025-06-06 | Original template system |
| WorkingCapital.md | 2.0.0 | versions/2025/Q2/WorkingCapital_2.0.0.md | 2025-06-06 | Documentation consolidation |
| WorkingCapital.md | 1.1.0 | versions/2025/Q2/WorkingCapital_1.1.0.md | 2025-06-05 | Added Phase 3-4 |
| WorkingCapital.md | 1.0.0 | versions/2025/Q2/WorkingCapital_1.0.0.md | 2025-06-01 | Initial version |
| standards.md | 1.0.0 | versions/2024/Q1/standards_1.0.0.md | 2024-01-18 | Initial version |

## System Version History
| Name | Version | Active Period | Current Status |
|------|---------|---------------|----------------|
| WORKCAP | 2.0.0 | 2024-present | Active - Current system |
| OPERCAP | 1.0.0 | 2025-06-01 to 2025-06-06 | Archived - Template system |

## Retention Policy
1. Reviews: 1 year
2. Reports: 2 years
3. Templates: Until superseded
4. Documentation: Keep all versions

## Archival Process
1. Move file to appropriate year/quarter folder
2. Update file_status to "archive"
3. Add entry to archive_log.md
4. Update references in active files

## Current Archives
| Original Location | Archive Location | Date Archived | Notes |
|------------------|------------------|---------------|--------|
| templates/opercap1.md | 2025/Q2/templates/opercap1.md | 2025-06-06 |
| templates/reports.md | 2025/Q2/templates/reports.md | 2025-06-06 |
| docs/folder-audit.md | archive/2025/Q2/folder-audit.md | 2025-06-06 | Content merged into standards.md |
