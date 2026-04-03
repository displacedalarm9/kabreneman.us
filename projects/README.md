---
last_updated: 2025-11-25
version: 1.0.0
file_status: protocol
---

# Projects Directory

This directory contains separate projects, each in its own subfolder. Projects should be self-contained but may depend on shared resources located in the `shared/` directory at the repository root.

## Structure

```
/projects/
  /project-name/     # Each project gets its own folder
    README.md        # Project documentation
    ...              # Project-specific files
```

## Creating a New Project

1. Create a new folder under `projects/` with a descriptive name
2. Add a `README.md` documenting the project's purpose
3. Reference shared dependencies from `../shared/` as needed

## Shared Dependencies

Projects can access shared resources via relative paths:
- `../shared/scripts/` - Shared executable scripts
- `../shared/data/` - Shared data files
- `../shared/utilities/` - Shared utility modules

## Current Projects

| Project | Description | Status |
|---------|-------------|--------|
| [workcap](workcap/README.md) | Project Working Capital - Financial tracking system | Active |

[See: ../shared/README.md for shared resource documentation]
