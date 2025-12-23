# kabreneman.us

Personal data management and documentation repository.

## Overview

This repository serves as a centralized system for:
- **System configuration and metadata** - Node configurations, topics, and settings
- **Documentation and procedures** - Standards, guidelines, and operational procedures
- **Management utilities** - Python scripts for file management and analysis
- **Templates** - Standardized templates for reports, tracking, and documentation
- **Archive** - Historical records and abandoned project documentation

## Repository Structure

```
kabreneman.us/
├── archive/          # Historical records and archived projects
├── configs/          # System configuration files (XML)
├── docs/             # Documentation (naming conventions, standards, history)
├── logs/             # Log file templates and README
├── procedures/       # Operational procedures (changeover, emergency, schedule)
├── scripts/          # Python utilities for file management
└── templates/        # Templates for reports and tracking
```

## Security & Privacy

⚠️ **Important**: This repository contains system files, templates, and documentation only. Personal financial data should be kept in the secure local backup directory (`~/secure-kabreneman-backup/`).

See `.gitignore` for comprehensive patterns that prevent sensitive data from being committed.

## Getting Started

### Prerequisites
- Python 3.7+ (for scripts)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/displacedalarm9/kabreneman.us.git
cd kabreneman.us

# Install Python dependencies (if using scripts)
pip install -r requirements.txt
```

### Using Scripts

**Metadata Wizard**:
```bash
python scripts/metadata_wizard.py
```
Interactive wizard for creating and managing YAML frontmatter metadata in markdown files. Supports both simple mode (basic frontmatter) and DOCSYS mode (full provenance tracking with TSN, cycles, and cross-references). See [docs/metadata-wizard.md](docs/metadata-wizard.md) for detailed usage.

**File Renaming Script**:
```bash
python scripts/fix_filenames.py [base_path]
```

**WorkCap Analyzer**:
```bash
python scripts/workcap_analyzer.py
```

## Documentation

- **Metadata Wizard Guide**: See [`docs/metadata-wizard.md`](docs/metadata-wizard.md)
- **File Naming Conventions**: See [`docs/filename.md`](docs/filename.md)
- **Report Standards**: See [`docs/report-standards.md`](docs/report-standards.md)
- **System History**: See [`docs/history.md`](docs/history.md)

## Related Information

### KABDMSV2 Integration

This repository has been integrated with KABDMSV2 (KAB Data Management System Version 2), which provides the management system/software component for organizing and managing personal data.

**Key Integration Points**:
- Node configuration files from KABDMSV2
- Topics and metadata (topics.json)
- Shared documentation standards

### Project Status & Reviews

**Current Status**: Active development on `pendingUpload` branch.

**Pending Reviews**:
| Issue | Description | Priority |
|-------|-------------|----------|
| KABDMSV2#9 | Integration review needed - verify data management system alignment | High |

**Recent Updates**:
- Accordion decision flowchart added (2025-11-25)
- Documentation automation guide created
- Issue templates and PR templates established

## Automated Tooling

This workspace includes the following automated tools and validation:

### Development Tools
| Tool | Purpose | Command |
|------|---------|---------|
| Black | Code formatting | `black scripts/` |
| Flake8 | Linting | `flake8 scripts/` |
| Pylint | Code analysis | `pylint scripts/` |
| Pytest | Testing | `pytest` |
| Mypy | Type checking | `mypy scripts/` |

### Installation
```bash
# Install development dependencies
pip install -r dev-requirements.txt
```

### Validation Commands
```bash
# Format code
black scripts/

# Run linting
flake8 scripts/
pylint scripts/

# Run type checking
mypy scripts/

# Run tests (when available)
pytest
```

## Contributing

When adding files to this repository:
1. Follow naming conventions documented in `docs/filename.md`
2. Use lowercase with hyphens for dates (`YYYY-MM-DD`)
3. Use underscores for word separators
4. Keep sensitive data in local secure backup only
5. Document procedures and templates appropriately

## License

See [LICENSE](LICENSE) file for details.
