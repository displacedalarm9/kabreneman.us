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
    import argparse
    
    # Get the repository root (two directories up from this script's location)
    script_dir = Path(__file__).resolve().parent
    default_base_path = script_dir.parent.parent
    
    parser = argparse.ArgumentParser(description='Fix file naming conventions')
    parser.add_argument('--base-path', type=str, default=str(default_base_path),
                        help='Base path for workspace (defaults to repository root)')
    args = parser.parse_args()
    
    rename_files(args.base_path, rename_map)
