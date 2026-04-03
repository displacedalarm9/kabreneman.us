---
last_updated: 2025-06-05
version: 1.2.0
file_status: active
---

# Project Working Capital - Documentation Standards

## References
[See: docs/filename.md for file naming rules and patterns]
[See: templates/index.md for template list]

## Important Note
All files MUST follow the naming conventions defined in `docs/filename.md`. See that document for:
- Character usage rules
- Date formatting standards
- General naming patterns

## Core Files
| File | Purpose |
|------|---------|
| templates/daily.md | Daily review template |
| templates/weekly.md | Weekly review template |
| templates/monthly.md | Monthly review template |
| templates/quarterly.md | Quarterly review template |
| changeover.md | Phase transition plans |
| standards.md | Documentation standards |
| templates/accounts.md | Account position template |
| templates/distribution.md | Payment allocation template |
| emergency.md | Contingency procedures |

## Standard Values
- Credit Cards: CR MCC ($450.11), CR VFB ($579.39)
- Buffer: $110/check minimum
- Income: $685-740/check range

## Calendar Standards
- Base Date: 6/5/25
- Phase 1: June-December 2025
- Phase 2: January-June 2026
- Phase 3: July-December 2026
- Phase 4: January 2027 onwards

## Folder Structure
/WORKCAP/
  /docs/         # Documentation and standards
  /procedures/   # System and project procedures
  /reviews/      # Position and status reviews
    /daily/      # Daily tracking
    /weekly/     # Weekly reviews  
    /monthly/    # Monthly analysis
    /quarterly/  # Phase assessments
  /templates/    # Document templates
    /review/     # Review templates
    /report/     # Report templates
    /data/       # Data templates
    /invest/     # Investment templates
  /archive/      # Archived files
    /YYYY/       # By year
      /QN/       # By quarter (Q1-Q4)
  /logs/         # Transaction tracking
    /journal/    # Daily transactions
    /bills/      # Payment records
    /debt/       # Debt tracking

## Document Types
Common document types in the workspace:

1. Reports and Reviews
   - Daily Reviews (reviews/daily/YYYY-MM/DD.md)
   - Weekly Reviews (reviews/weekly/YYYY-MM/DD.md)
   - Monthly Reviews (reviews/monthly/YYYY-MM.md)
   - Quarterly Reviews (reviews/quarterly/YYYY-QX.md)
   - Variance Reports (reviews/variance/YYYY-MM/DD.md)
   - Utility Analysis (reviews/utilities/YYYY-MM/provider.md)
   - Status Reports (reviews/status/YYYY-MM/DD.md)

2. Templates and Forms
   - Report Templates (templates/[type].md)
   - Distribution Forms (templates/distribution.md)
   - Review Forms (templates/[period].md)
   - Account Forms (templates/accounts.md)

3. Procedures and Documentation
   - System Protocols (/procedures/system/)
   - Project Protocols (/procedures/project/)
   - Emergency Procedures (/procedures/emergency/)

## File Organization
1. Reports and Reviews
   - Location: `/reviews/[type]/YYYY-MM/`
   - For naming pattern, see docs/filename.md
   - Example: `/reviews/variance/2025-06/2025-06-21_daily.md`

2. Templates
   - Location: `/templates/`
   - For naming pattern, see docs/filename.md
   - Update: matrix.md for requirements

3. Procedures
   - Location: `/procedures/[category]/`
   - For naming pattern, see docs/filename.md
   - Update: standards.md for changes

## Template Index
1. Report Templates
   - `/templates/review/daily.md`: Daily position checklist
   - `/templates/review/weekly.md`: Weekly review format
   - `/templates/review/monthly.md`: Monthly review format 
   - `/templates/review/quarterly.md`: Quarter review format
   - `/templates/report/variance.md`: Variance tracking
   - `/templates/report/status.md`: Status reporting

2. Data Templates
   - `/templates/data/accounts.md`: Account positions
   - `/templates/data/utilities.md`: Utility tracking
   - `/templates/data/distribution.md`: Payment allocation
   - `/templates/data/obligations.md`: Obligation tracking

3. Special Templates  
   - `/templates/invest/sidu.md`: Discretionary usage
   - `/templates/invest/investment.md`: Investment tracking

## Report Standards
1. Daily Reviews
   - Location: reviews/daily/YYYY-MM/DD.md
   - Template: templates/daily.md
   - Updates: accounts.md, matrix.md

2. Weekly Reviews
   - Location: reviews/weekly/YYYY-MM/DD.md
   - Template: templates/weekly.md
   - Updates: matrix.md

3. Monthly Reviews
   - Location: reviews/monthly/YYYY-MM.md
   - Template: templates/monthly.md
   - Updates: WorkingCapital.md

4. Status Reports
   - Location: reviews/status/YYYY-MM/DD.md
   - Template: templates/status.md
   - Updates: emergency.md if needed

## Status Definitions
| Status | Definition | Required Action |
|--------|------------|----------------|
| OK | Within tolerance | Continue monitoring |
| WATCH | Near tolerance limit | Increase monitoring |
| ALERT | Outside tolerance | Immediate action required |

## File Status Definitions

| Status | Description | Example Files |
|--------|-------------|---------------|
| core | System foundation documents | WorkingCapital.md |
| protocol | System procedures & rules | standards.md, emergency.md |
| template | Reusable document formats | templates/*.md |
| report | Generated from templates | reviews/*/*.md |
| log | Tracking & history files | archive/README.md |
| review | Analysis documents | reviews/adherence/*.md |
| archive | Historical versions | archive/*/*.md |

## Status Determination Rules
1. Core Status
   - Project definition files
   - Phase transition documents
   - Critical path files

2. Protocol Status
   - System procedures
   - Documentation standards
   - Operating rules

3. Template Status
   - All files in /templates/
   - Form definitions
   - Report structures

4. Report Status
   - All generated reviews
   - Position statements
   - Variance tracking

5. Log Status
   - Archive indexes
   - Change histories
   - Version tracking

6. Review Status
   - Analysis documents
   - Adherence checks
   - Progress tracking

7. Archive Status
   - Previous versions
   - Deprecated files
   - Historical records

## File Headers
```yaml
---
last_updated: YYYY-MM-DD
version: [major].[minor].[patch]
file_status: [report|template|protocol|active]
---
```

## Cross-Reference Rules
1. Use format: [See: docs/filename.md]
2. Always reference primary source files
3. Never duplicate data - link instead
