# Data Directory

This directory is for storing sensitive local data files that should NOT be committed to version control.

## Contents

This directory should contain:
- `sysinfo.txt` - System information export
- `system-info-formatted.md` - Formatted system information
- Any other personal or sensitive data files

## Important

All files in this directory are gitignored. They exist only on your local machine.

## Setting Up Your Local Data

1. Download or export your system information
2. Place the files in this directory
3. The application will read from this location

## Backing Up

Since these files are not in version control, make sure to:
- Keep local backups
- Store copies in a secure location
- Do not share files containing personal information
