---
last_updated: 2025-06-06
version: 1.0.0
file_status: template
---

# Report Generation Guide

## File Structure
/reviews/
  /{type}/      # variance, obligations, etc.
    /{year}-{month}/
      {date}-{report}.md

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

[See: standards.md for naming conventions]
[See: templates/index.md for template list]
