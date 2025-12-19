#!/usr/bin/env python3
"""
Metadata Wizard - Interactive tool for managing YAML frontmatter in markdown files

This wizard helps create and update YAML metadata headers in markdown files,
ensuring consistency across templates and documentation.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

class MetadataWizard:
    """Interactive wizard for managing file metadata"""
    
    VALID_FILE_STATUSES = ['template', 'protocol', 'active', 'report', 'archive']
    
    def __init__(self):
        self.metadata = {}
        
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 60)
        print("METADATA WIZARD")
        print("=" * 60)
        print("\nThis wizard helps you add or update YAML frontmatter metadata")
        print("in markdown files for the kabreneman.us repository.\n")
    
    def get_file_path(self):
        """Prompt user for file path"""
        while True:
            file_path = input("\nEnter the file path (relative or absolute): ").strip()
            
            if not file_path:
                print("Error: File path cannot be empty.")
                continue
            
            path = Path(file_path)
            
            # Handle relative paths
            if not path.is_absolute():
                path = Path.cwd() / path
            
            if not path.exists():
                create = input(f"\nFile does not exist. Create it? (y/n): ").strip().lower()
                if create == 'y':
                    return path, None
                else:
                    continue
            
            if not path.is_file():
                print("Error: Path must be a file, not a directory.")
                continue
            
            if path.suffix.lower() != '.md':
                print("Warning: File does not have .md extension.")
                proceed = input("Continue anyway? (y/n): ").strip().lower()
                if proceed != 'y':
                    continue
            
            # Read existing content
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return path, content
    
    def parse_existing_metadata(self, content):
        """Extract existing YAML frontmatter if present"""
        if not content or not content.startswith('---'):
            return None, content
        
        # Find the end of YAML frontmatter
        match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            body_content = match.group(2)
            
            # Parse YAML fields
            metadata = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            
            return metadata, body_content
        
        return None, content
    
    def prompt_metadata_fields(self, existing_metadata=None):
        """Interactively prompt for metadata fields"""
        print("\n" + "=" * 60)
        print("METADATA FIELDS")
        print("=" * 60)
        
        if existing_metadata:
            print("\nExisting metadata found:")
            for key, value in existing_metadata.items():
                print(f"  {key}: {value}")
            print("\nPress Enter to keep existing values or enter new ones.\n")
        
        # Last updated date
        default_date = datetime.now().strftime('%Y-%m-%d')
        if existing_metadata and 'last_updated' in existing_metadata:
            current_date = existing_metadata['last_updated']
            date_input = input(f"Last updated date [{current_date}] (YYYY-MM-DD): ").strip()
            self.metadata['last_updated'] = date_input if date_input else current_date
        else:
            date_input = input(f"Last updated date [{default_date}] (YYYY-MM-DD): ").strip()
            self.metadata['last_updated'] = date_input if date_input else default_date
        
        # Version
        default_version = '1.0.0'
        if existing_metadata and 'version' in existing_metadata:
            current_version = existing_metadata['version']
            version_input = input(f"Version [{current_version}]: ").strip()
            self.metadata['version'] = version_input if version_input else current_version
        else:
            version_input = input(f"Version [{default_version}]: ").strip()
            self.metadata['version'] = version_input if version_input else default_version
        
        # File status
        print(f"\nValid file statuses: {', '.join(self.VALID_FILE_STATUSES)}")
        default_status = 'template'
        if existing_metadata and 'file_status' in existing_metadata:
            current_status = existing_metadata['file_status']
            status_input = input(f"File status [{current_status}]: ").strip()
            status = status_input if status_input else current_status
        else:
            status_input = input(f"File status [{default_status}]: ").strip()
            status = status_input if status_input else default_status
        
        while status not in self.VALID_FILE_STATUSES:
            print(f"Error: Invalid file status. Must be one of: {', '.join(self.VALID_FILE_STATUSES)}")
            status = input("File status: ").strip()
        
        self.metadata['file_status'] = status
        
        # Custom fields
        print("\nAdd custom fields? (y/n): ", end='')
        if input().strip().lower() == 'y':
            while True:
                key = input("  Field name (or press Enter to finish): ").strip()
                if not key:
                    break
                value = input(f"  Value for '{key}': ").strip()
                self.metadata[key] = value
    
    def generate_yaml_header(self):
        """Generate YAML frontmatter string"""
        yaml_lines = ['---']
        for key, value in self.metadata.items():
            yaml_lines.append(f"{key}: {value}")
        yaml_lines.append('---')
        return '\n'.join(yaml_lines)
    
    def preview_metadata(self):
        """Display preview of metadata"""
        print("\n" + "=" * 60)
        print("METADATA PREVIEW")
        print("=" * 60)
        print("\n" + self.generate_yaml_header())
        print()
    
    def confirm_action(self, action="save"):
        """Ask user to confirm the action"""
        response = input(f"\nProceed with {action}? (y/n): ").strip().lower()
        return response == 'y'
    
    def save_file(self, file_path, content):
        """Save file with metadata"""
        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Combine metadata and content
        yaml_header = self.generate_yaml_header()
        
        if content is None:
            # New file - create with just metadata and placeholder
            full_content = yaml_header + "\n\n# [TITLE]\n\n[Content goes here]\n"
        else:
            # Existing file - prepend metadata
            full_content = yaml_header + "\n\n" + content
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"\n✓ File saved: {file_path}")
    
    def run(self):
        """Run the wizard"""
        self.display_welcome()
        
        # Get file path
        file_path, content = self.get_file_path()
        
        # Parse existing metadata if any
        existing_metadata, body_content = self.parse_existing_metadata(content) if content else (None, None)
        
        if existing_metadata:
            print(f"\n✓ Found existing metadata in file")
        
        # Prompt for metadata
        self.prompt_metadata_fields(existing_metadata)
        
        # Preview
        self.preview_metadata()
        
        # Confirm and save
        if self.confirm_action("save"):
            self.save_file(file_path, body_content)
            print("\n✓ Metadata wizard completed successfully!")
        else:
            print("\n✗ Operation cancelled.")
            sys.exit(0)


def main():
    """Main entry point"""
    wizard = MetadataWizard()
    try:
        wizard.run()
    except KeyboardInterrupt:
        print("\n\n✗ Wizard cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
