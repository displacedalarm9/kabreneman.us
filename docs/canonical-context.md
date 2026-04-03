---
last_updated: 2026-04-03
version: 1.0.0
file_status: active
---

# Canonical Context Document

> **Hub Document** — This is the single source of truth for all AI assistant context about this repository.
> Platform-specific instruction files (spokes) are derived from this document.
>
> **Update procedure**: When this repository changes, update this document first, then propagate
> updates to each spoke file:
> - `.github/copilot-instructions.md` — GitHub Copilot spoke
> - `CLAUDE.md` — Claude (Anthropic) spoke

## 1. Project Identity

**Repository**: kabreneman.us  
**System**: KABDMSV2 (KAB Data Management System Version 2)  
**Purpose**: Personal data management system split across two repositories:

| Repository | Contains | Visibility |
|------------|----------|------------|
| `kabreneman.us` | System config, templates, procedures, management utilities | Public |
| External data repo | Actual financial records, logs, personal documents | Private/local only |

## 2. Repository Structure

```
kabreneman.us/
├── .github/
│   ├── copilot-instructions.md   # GitHub Copilot spoke (derived from this doc)
│   ├── ISSUE_TEMPLATE/           # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md  # PR template
├── archive/                      # Historical records and archived projects
├── configs/                      # Node configuration files (XML)
├── data/                         # Local-only sensitive data (gitignored contents)
├── docs/                         # Documentation and standards
│   ├── canonical-context.md      # Canonical hub document
│   ├── automation-guide.md       # Work documentation automation
│   ├── filename.md               # File naming conventions
│   ├── folder-audit.md           # Folder structure audit
│   ├── history.md                # System terminology history
│   ├── metadata-wizard.md        # Metadata wizard usage guide
│   ├── report-standards.md       # Report generation standards
│   └── project_support/          # Project-support artifacts (DOCSYS/UNISYS canonized)
│       └── copilot/              # Copilot activity records (TSN:0001–TSN:0003)
├── logs/                         # Transaction log templates
├── procedures/                   # Operational workflows
│   ├── changeover.md             # Phase transition plans
│   ├── changes.md                # Change management
│   ├── emergency.md              # Emergency protocols
│   ├── matrix.md                 # Distribution matrix and tolerances
│   └── schedule.md               # Review schedule
├── projects/                     # Project-specific directories
│   └── workcap/                  # WORKCAP project documentation
├── reports/                      # Generated analysis reports
├── reviews/                      # Position and status reviews
├── scripts/                      # Python utilities
│   ├── fix_filenames.py          # File rename utility
│   ├── metadata_wizard.py        # Metadata wizard
│   └── workcap_analyzer.py       # Working capital analysis
├── shared/                       # Shared scripts and data
├── templates/                    # Standardized templates
├── utilities/                    # Utility bill records
├── allocation.md                 # Income allocation protocol template
├── cashflowsfy26.md              # Cash flows statement template
├── CLAUDE.md                     # Claude (Anthropic) spoke (derived from this doc)
├── debts.csv                     # Debt tracking data
├── expenses.md                   # Fixed expenses tracking
├── obligations.md                # Fixed obligations protocol template
├── obligationadherence.md        # Obligation adherence tracking
├── OPERCAP1.xlsm                 # Original OPERCAP spreadsheet (archived)
├── progress.md                   # Project adherence schedule
├── README.md                     # Repository overview
├── review.md                     # Review schedule
├── standards.md                  # Documentation standards
├── topics.json                   # KABDMSV2 metadata
├── TRANSFER_CHECKLIST.md         # Repository file audit and transfer checklist
└── WorkingCapital.md             # Core project overview and execution protocol
```

## 3. Architecture and Data Flow

### Core Components

- **Node Configurations** (`configs/`): XML files defining system nodes with hardware specs,
  software stacks, and environment settings. Each node uses a unique CSN
  (Customer Serial Number) formatted as `ID-NODE-[TYPE]-[NUM]`. Environment tags classify
  nodes by purpose: OPS=operations, ARC=archival, VR=virtual reality.

- **Templates** (`templates/`): Standardized markdown templates for financial tracking,
  reports, and reviews. Designed to be copied to the external data repository with date
  prefixes (e.g., `templates/daily.md` → `2025-11-25_daily.md`).

- **Procedures** (`procedures/`): Operational workflows including phase transitions,
  emergency protocols, scheduling matrices, and distribution rules.

- **Scripts** (`scripts/`): Python utilities for file management and analysis.
  - `fix_filenames.py`: Renames files to match naming conventions.
  - `workcap_analyzer.py`: Analyzes working capital and generates reports.

### Python Dependencies

```bash
pip install -r requirements.txt      # Core runtime dependencies
pip install -r dev-requirements.txt  # Development/analysis tools
```

## 4. File Naming Conventions

**Pattern**: `[Type]_[ID/Date]_[Description].[extension]`

### Rules
- Lowercase characters only
- Hyphens (`-`) for date separators only (format: `YYYY-MM-DD`)
- Underscores (`_`) for word separators
- No spaces in filenames
- Concise and descriptive names

### Date Formats
| Scope | Format | Example |
|-------|--------|---------|
| Full date | `YYYY-MM-DD` | `2025-06-06` |
| Month | `YYYY-MM` | `2025-06` |
| Quarter | `YYYY-QN` | `2025-Q2` |
| Year | `YYYY` | `2025` |

### Examples
- `2025-06-06_daily.md` — daily review file
- `config_NODE-OPS-001_Legion5Gen10.xml` — node config file
- `2025-06-21_variance.md` — variance report

## 5. Markdown Frontmatter Standard

All documentation files use frontmatter:

```yaml
---
last_updated: YYYY-MM-DD
version: X.Y.Z
file_status: [template|active|protocol|archive]
---
```

## 6. Cross-Reference Pattern

Files reference related documentation using inline links:

```markdown
[See: procedures/matrix.md for tolerances]
[See: procedures/emergency.md for alerts]
```

## 7. Status Indicators

Templates use consistent status indicators throughout:
- Completion: `[✓/-]`
- Health: `[OK/WATCH/ALERT]`
- Progress: `[DONE/PENDING]`

## 8. Financial Phase System

The system operates on four phases defined in `procedures/changeover.md`:

| Phase | Period | Buffer Target | Key Goal |
|-------|--------|---------------|----------|
| 1. Debt Control | June–Dec 2025 | $110/check | Stabilize cash flow |
| 2. Debt Reduction | Jan–June 2026 | $250/check | Resolve collections |
| 3. Build Credit | July–Dec 2026 | $500/check | Credit score +50 pts |
| 4. Build Wealth | Jan 2027+ | Long-term | Savings and investment |

### Distribution Matrix (`procedures/matrix.md`)
- Daily variance tolerance: ±$50 cash position, ±$25 credit usage
- Weekly variance tolerance: ±$100 distribution total, 30% max credit utilization
- Monthly variance tolerance: -0%/+25% debt reduction, -5%/+20% savings goals

### Emergency Triggers (`procedures/emergency.md`)
- Buffer drops below $50
- Credit utilization exceeds 95%
- Payment default imminent

## 9. Report Structure

```
/reviews/
  /variance/YYYY-MM/      # Monthly variance analysis
  /status/YYYY-MM/        # Status reports
  /accounts/YYYY-MM/      # Account tracking
  /utilities/YYYY-MM/     # Utility bill analysis
  /obligations/           # Obligation reviews (daily/weekly/monthly/quarterly)
  /adherence/             # Phase compliance tracking
```

### Report File Naming
- Review reports: `YYYY-MM-DD_[type].md`
- Analysis reports: `YYYY-MM_[provider].md`

## 10. Security Boundaries

- **Never commit sensitive data** — financial records, account numbers, balances
- Actual data lives in the private external repository or `~/secure-kabreneman-backup/`
- Templates, procedures, and system config only in this repository
- `.gitignore` contains comprehensive patterns that prevent accidental data commits

## 11. Work Documentation Workflow

### Planned Work (Recommended)
```
Create Issue → Do Work → Create PR → Link to Issue → Merge
```

### Ad-Hoc Work (Acceptable)
```
Do Work → Commit → Create "[DONE]" Documentation Issue
```

Use the Work Documentation issue template (`.github/ISSUE_TEMPLATE/work-documentation.md`).

### Commit Message Conventions
- `Fixes #123` — closes issue when merged
- `Closes #123` — closes issue when merged
- `Related to #123` — links without closing

## 12. Configuration Node Format

Node configs (`configs/*.xml`) use standardized XML sections:
- `System` — CSN, environment tag, description
- `Hardware` — CPU, RAM, storage specs
- `Software` — OS, installed tools, stacks
- `ProfileOverlay` — user and environment settings
- `Networking` — network configuration

Example CSN values: `ID-NODE-OPS-001`, `ID-NODE-VR-002`, `ID-NODE-ARC-003`

## 13. Template Usage Pattern

Templates in `templates/` are copied to the external data repository with date prefixes.

| Template | Target | Notes |
|----------|--------|-------|
| `templates/daily.md` | `YYYY-MM-DD_daily.md` | Daily review |
| `templates/weekly.md` | `YYYY-MM-DD_weekly.md` | Weekly summary |
| `templates/monthly.md` | `YYYY-MM_monthly.md` | Monthly review |
| `templates/variance.md` | `YYYY-MM-DD_variance.md` | Variance report |
| `templates/utilities.md` | `YYYY-MM_[provider].md` | Utility bill |

## 14. KABDMSV2 Integration Metadata

- `topics.json`: Project metadata, system name tags, and link to data repository
- System names in use:
  - **WORKCAP** (Active): Working Capital System, current version
  - **OPERCAP** (Archived 2025-06-06): Original template system v1
  - **Adherence System** (Active): Phase compliance tracking
