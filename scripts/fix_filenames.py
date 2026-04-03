from pathlib import Path
import shutil
import re

# File renames to be performed
rename_map = {
    'reviews/accounts/2025-06/daily-06-06.md': 'reviews/accounts/2025-06/2025-06-06_daily.md',
    'reviews/adherence/2025-06-06.md': 'reviews/adherence/2025-06-06_adherence.md',
    'reviews/obligations/2025-06-06.md': 'reviews/obligations/2025-06-06_obligations.md',
    'reviews/status/2025-06-06.md': 'reviews/status/2025-06-06_status.md',
    'reviews/utilities/2025-06/evergy.md': 'reviews/utilities/2025-06/2025-06-06_evergy.md',
    'reviews/utilities/2025-06/kansas-gas.md': 'reviews/utilities/2025-06/2025-06-06_gas.md',
    'reviews/utilities/2025-06/water.md': 'reviews/utilities/2025-06/2025-06-06_water.md',
    'reviews/variance/2025-06/daily-06-06.md': 'reviews/variance/2025-06/2025-06-06_variance.md',
    'reviews/variance/2025-06/daily-06-21.md': 'reviews/variance/2025-06/2025-06-21_variance.md'
}

def rename_files(base_path, rename_map):
    """Rename files according to the provided mapping"""
    base = Path(base_path)
    for old_path, new_path in rename_map.items():
        old_file = base / old_path
        new_file = base / new_path
        if old_file.exists():
            # Create parent directories if they don't exist
            new_file.parent.mkdir(parents=True, exist_ok=True)
            # Rename file
            shutil.move(str(old_file), str(new_file))
            print(f"Renamed: {old_path} -> {new_path}")

if __name__ == '__main__':
    import sys
    # Default to current directory if no path provided
    base_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    rename_files(base_path, rename_map)
    print(f"\nRename operation completed for base path: {base_path}")
