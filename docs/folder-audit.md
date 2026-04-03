---
last_updated: 2026-04-03
version: 1.1.0
file_status: protocol  # Confirmed as protocol
---

# Folder Structure Analysis

## References
[See: docs/filename.md for naming conventions]
[See: templates/index.md for template list]
[See: archive/README.md for retention policy]

## Current Structure
/kabreneman.us/
  /archive/          # Archived files
    /2025/           # By year
      /Q2/           # By quarter
      /Q4/
  /configs/          # Node configuration files (XML)
  /data/             # Local-only sensitive data (gitignored)
  /docs/             # Documentation and standards
    /project_support/  # Project-support artifacts
      /copilot/      # Copilot activity records
  /logs/             # Transaction log templates
  /procedures/       # System and project procedures
  /projects/         # Project directories
    /workcap/        # WORKCAP project
  /reports/          # Generated analysis reports
    /analysis/       # WorkCap analysis outputs
  /reviews/          # Position and status reviews
    /accounts/YYYY-MM/
    /adherence/
    /obligations/
    /status/
    /utilities/YYYY-MM/
    /variance/YYYY-MM/
  /scripts/          # Python utilities
  /shared/           # Shared scripts and data
    /data/
    /scripts/
    /utilities/
  /templates/        # Document templates
    /data/           # Data templates
    /report/         # Report templates
  /utilities/        # Utility bill records
    /YYYY-MM/
