# kabreneman.us

Personal data management system.

## Table of Contents

- [Overview](#overview)
- [Security Guidelines](#security-guidelines)
- [Environment Setup](#environment-setup)
- [Data Files](#data-files)
- [Project Structure](#project-structure)

## Overview

This repository serves as the management software for personal data and system information. It is designed to help organize and manage various data files while keeping sensitive information secure and private.

## Security Guidelines

### Sensitive Data Protection

This repository is configured to **exclude sensitive data files** from version control. The following types of files should NEVER be committed:

- **Environment files** (`.env`, `.env.local`, etc.)
- **System information files** (`sysinfo.txt`, `system-info-*.md`)
- **Credentials and keys** (`*.key`, `*.pem`, `credentials.json`)
- **Database files** (`*.sqlite`, `*.db`, `*.mdb`)
- **Personal data exports** (`*personal*.json`, `*private*.json`)

### What IS Safe to Commit

- Configuration templates (`.env.example`)
- Documentation files (`.md`, `.txt` without sensitive data)
- Application source code
- Build configurations (without embedded secrets)

## Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/displacedalarm9/kabreneman.us.git
   cd kabreneman.us
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual configuration values
   ```

3. **Store sensitive data locally:**
   - Create a `data/` directory in your local clone
   - Place sensitive files like `sysinfo.txt` there
   - These files are gitignored and will NOT be uploaded

## Data Files

### Local Data Storage

Sensitive data files should be stored locally and NOT committed to the repository:

| File Type | Location | Purpose |
|-----------|----------|---------|
| System info | `data/sysinfo.txt` | System configuration details |
| Personal configs | `data/` | Personal configuration files |
| Exports | `data/exports/` | Data exports and backups |

### Topics Configuration

The `topics.json` file contains non-sensitive metadata about project topics and can be safely committed.

## Project Structure

```
kabreneman.us/
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules (includes security patterns)
├── README.md             # This file
├── LICENSE               # Project license
├── topics.json           # Project topics metadata
├── accordionDecision/    # Decision documentation
└── data/                 # Local-only data (gitignored)
    ├── sysinfo.txt       # System information (local only)
    └── exports/          # Data exports (local only)
```

## Contributing

When contributing to this project:

1. **Never commit sensitive data** - Check `.gitignore` patterns
2. **Use environment variables** - Store secrets in `.env` (gitignored)
3. **Review changes** - Use `git diff` before committing
4. **Document sensitive fields** - Update `.env.example` when adding new config

## License

See [LICENSE](LICENSE) file for details.
