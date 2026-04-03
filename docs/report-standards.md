---
last_updated: 2025-06-06
version: 1.0.0
file_status: active
---

# Report Generation Standards

[See: standards.md for naming conventions]
[See: templates/index.md for template list]

## File Naming Conventions
1. Review Reports
   - Pattern: `YYYY-MM-DD_[type].md`
   - Example: `2025-06-21_daily.md`

2. Analysis Reports
   - Pattern: `YYYY-MM_[provider].md`
   - Example: `2025-06_water.md`

## Standard Folder Structure
/reviews/
  /variance/     # Variance analysis
    /YYYY-MM/    # Organized by month
  /status/       # Status reports
    /YYYY-MM/
  /accounts/     # Account tracking
    /YYYY-MM/
  /utilities/    # Utility reports
    /YYYY-MM/

## Report Types
1. Daily Reviews
   - Location: reviews/daily/YYYY-MM/DD.md
   - Template: templates/daily.md
   - Updates: accounts.md, matrix.md

2. Variance Reports
   - Location: reviews/variance/YYYY-MM/DD.md
   - Template: templates/variance.md
   - Updates: emergency.md if needed

3. Utility Reports
   - Location: utilities/YYYY-MM/provider.md
   - Template: templates/utilities.md
   - Updates: progress.md for budgets