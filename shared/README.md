---
last_updated: 2025-11-25
version: 1.0.0
file_status: protocol
---

# Shared Resources Directory

This directory contains executables, code, and data files that are shared across multiple projects. These serve as dependencies that can be accessed by any project in the `/projects/` directory.

## Structure

```
/shared/
  /scripts/      # Executable scripts and command-line tools
  /data/         # Shared data files used by multiple projects
  /utilities/    # Reusable utility modules and libraries
  README.md      # This documentation file
```

## Subdirectories

### /scripts/
Contains executable scripts that can be run directly or called by projects.
- Python scripts
- Shell scripts
- Automation tools

### /data/
Contains shared data files that multiple projects may need access to.
- Common reference data
- Configuration templates
- Shared datasets

### /utilities/
Contains reusable utility modules and libraries that projects can import.
- Python modules
- Helper functions
- Common libraries

## Usage

Projects can access shared resources using relative paths:

```python
# From a project in /projects/myproject/
import sys
sys.path.insert(0, '../../shared/utilities')
from myutility import helper_function
```

Or reference data files:

```python
DATA_PATH = '../../shared/data/mydata.csv'
```

## Adding Shared Resources

1. Place the resource in the appropriate subdirectory
2. Document its purpose in this README or in subdirectory-specific documentation
3. Update any projects that should use the shared resource

[See: ../projects/README.md for project documentation]
