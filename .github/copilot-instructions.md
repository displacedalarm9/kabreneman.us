# Copilot Instructions for kabreneman.us

## Project Overview
This is a **personal data management system (KABDMSV2)** split into two repositories:
- This repo: System configuration, templates, procedures, and management utilities
- External repo: Actual sensitive data (financial records, logs) - kept private and local

## Architecture & Data Flow

### Core Components
- **Node Configurations** (`configs/`): XML files defining system nodes with hardware specs, software stacks, and environment settings
- **Templates** (`templates/`): Standardized markdown templates for financial tracking, reports, and reviews
- **Procedures** (`procedures/`): Operational workflows including phase transitions, emergency protocols, and scheduling matrices
- **Scripts** (`scripts/`): Python utilities for file management, analysis, and automated workflows

### Critical File Naming Convention
File naming patterns are **category-specific** but share common rules:
- Dates: `YYYY-MM-DD` (hyphens only)
- Words: underscores for separation

**Time-series markdown (templates, logs, reports)**  
- Pattern: `[Date]_[Description].md`
- Example: `2025-06-06_daily.md`

**Node configuration XML files (`configs/`)**  
- Pattern: `config_[CSN]_[HostModel].xml`
- `CSN`: matches `ID-NODE-[TYPE]-[NUM]` (see Configuration Management below)
- Example: `config_NODE-OPS-001_Legion5Gen10.xml`
## Development Workflows

### File Management Scripts
```bash
# Fix filename conventions across data repository
python scripts/fix_filenames.py [base_path]

# Analyze working capital and generate reports
python scripts/workcap_analyzer.py
```

### Template Usage Pattern
Templates in `templates/` are designed for copying to data repository with date prefixes:
- `templates/daily.md` → `2025-11-25_daily.md` in data repo
- Follow markdown frontmatter structure (last_updated, version, file_status)

### Report Generation Structure
```
/reviews/
  /variance/YYYY-MM/     # Monthly variance analysis
  /status/YYYY-MM/       # Status reports  
  /accounts/YYYY-MM/     # Account tracking
  /utilities/YYYY-MM/    # Utility bill analysis
```

## Project-Specific Patterns

1. **Debt Control**: Establishes an initial per-paycheck buffer and stabilizes cash flow.
2. **Debt Reduction**: Increases the buffer and accelerates payoff of existing obligations.
3. **Build Credit**: Maintains a larger buffer while focusing on improving credit position.
4. **Build Wealth**: Long-term growth, savings, and investment focus.

### Financial Phase System
The system operates on 4 phases (defined in `procedures/changeover.md`):
1. **Debt Control** (June-Dec 2025): $110/check buffer target
2. **Debt Reduction** (Jan-June 2026): $250/check buffer target  
3. **Build Credit** (July-Dec 2026): $500/check buffer target
4. **Build Wealth** (Jan 2027+): Long-term growth

### Security Boundaries
- **Never commit sensitive data** - use local `~/secure-kabreneman-backup/` directory
- Templates and procedures only - actual financial data stays private
- `.gitignore` prevents accidental data commits

## Integration Points

### KABDMSV2 Metadata
- `topics.json`: Contains project metadata and links to data repository
- Separation of concerns: this repo = management system, external repo = actual data

### Python Dependencies
- `requirements.txt`: Core dependencies for file management scripts
- `dev-requirements.txt`: Development and analysis tools
- Scripts expect data repository structure for analysis workflows

## Key Conventions

### Markdown Structure
All documentation uses frontmatter:
```yaml
---
last_updated: YYYY-MM-DD
version: X.Y.Z
file_status: [template|active|protocol|archive]
---
```

### Cross-Reference Pattern
Files frequently reference related documentation:
```markdown
[See: procedures/matrix.md for tolerances]
[See: procedures/emergency.md for alerts]
```

### Status Tracking
Templates use consistent status indicators: `[✓/-]`, `[OK/WATCH/ALERT]`, `[DONE/PENDING]`

## When Making Changes
1. Follow naming conventions in `docs/filename.md`
2. Update version numbers and last_updated dates in frontmatter
3. Maintain cross-references between related files
4. Test scripts against sample data structure (never commit actual data)
5. Use PR template checklist for sensitive data verification