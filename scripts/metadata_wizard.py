#!/usr/bin/env python3
"""
Metadata Wizard - Interactive tool for managing YAML frontmatter in markdown files

This wizard helps create and update YAML metadata headers in markdown files,
ensuring consistency across templates and documentation. Supports both simple
markdown frontmatter and full DOCSYS/UNISYS metadata schemas.
"""

import re
import sys
import yaml
import random
from pathlib import Path
from datetime import datetime

class MetadataWizard:
    """Interactive wizard for managing file metadata"""
    
    # Simple mode (markdown frontmatter)
    VALID_FILE_STATUSES = ['template', 'protocol', 'active', 'report', 'archive']
    
    # DOCSYS mode
    SYSTEMS = ['WORKCAP', 'UNISYS', 'DOCSYS', 'REDOREPO', 'NDS', 'FINTRACK']
    ARTIFACT_TYPES = [
        'ProjectSupport', 'Finance', 'Legal', 'Medical', 'Education', 
        'Employment', 'Home', 'Process', 'SystemArchitecture', 
        'CanonPolicy', 'StoryArchitecture'
    ]
    SUBTYPES = {
        'ProjectSupport': ['ActivityLedger', 'ConversationLog', 'Documentation'],
        'Finance': ['Invoice', 'UtilityBill', 'Statement', 'Report']
    }
    RETENTION_CLASSES = ['preserved', 'versioned', 'consolidated', 'archived', 'deleted']
    
    def __init__(self):
        self.metadata = {}
        self.mode = 'simple'  # 'simple' or 'docsys'
        
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 70)
        print("METADATA WIZARD - DOCSYS/UNISYS Integration")
        print("=" * 70)
        print("\nThis wizard helps you create or update metadata for files in the")
        print("kabreneman.us repository with DOCSYS provenance tracking.\n")
        
    def select_mode(self):
        """Select wizard mode"""
        print("Select metadata mode:")
        print("  1. Simple (markdown frontmatter only)")
        print("  2. DOCSYS (full provenance tracking with TSN, cycles, etc.)")
        
        while True:
            choice = input("\nMode [1/2]: ").strip()
            if choice == '1':
                self.mode = 'simple'
                return
            elif choice == '2':
                self.mode = 'docsys'
                return
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
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
            
            try:
                # Try to parse as YAML first (for DOCSYS mode)
                metadata = yaml.safe_load(yaml_content)
                if isinstance(metadata, dict):
                    return metadata, body_content
            except yaml.YAMLError:
                # Fall back to simple parsing if YAML parsing fails
                pass
            
            # Fall back to simple key:value parsing
            metadata = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            
            return metadata, body_content
        
        return None, content
    
    def generate_tsn(self):
        """Generate a Trace Sequence Number (TSN)"""
        # Format: YYYYMMDD-XXXX where XXXX is a random 4-digit hex
        date_part = datetime.now().strftime('%Y%m%d')
        random_part = format(random.randint(0, 65535), '04X')
        return f"{date_part}-{random_part}"
    
    def prompt_docsys_metadata(self, existing_metadata=None):
        """Prompt for DOCSYS/UNISYS metadata fields"""
        print("\n" + "=" * 70)
        print("DOCSYS METADATA FIELDS")
        print("=" * 70)
        
        if existing_metadata:
            print("\nExisting metadata found. Press Enter to keep values.\n")
        
        # System
        print(f"\nAvailable systems: {', '.join(self.SYSTEMS)}")
        default_system = existing_metadata.get('system', 'UNISYS') if existing_metadata else 'UNISYS'
        system = input(f"System [{default_system}]: ").strip() or default_system
        self.metadata['system'] = system
        
        # Cycle
        default_cycle = existing_metadata.get('cycle', 'Continuous') if existing_metadata else 'Continuous'
        cycle = input(f"Cycle (e.g., 'Year 1', 'Year 2', 'Continuous') [{default_cycle}]: ").strip() or default_cycle
        self.metadata['cycle'] = cycle
        
        # Artifact type
        print(f"\nArtifact types: {', '.join(self.ARTIFACT_TYPES)}")
        default_type = existing_metadata.get('artifact_type', 'ProjectSupport') if existing_metadata else 'ProjectSupport'
        artifact_type = input(f"Artifact type [{default_type}]: ").strip() or default_type
        self.metadata['artifact_type'] = artifact_type
        
        # Subtype
        if artifact_type in self.SUBTYPES:
            print(f"Subtypes for {artifact_type}: {', '.join(self.SUBTYPES[artifact_type])}")
            subtype_input = input("Subtype(s) (comma-separated): ").strip()
            if subtype_input:
                self.metadata['subtype'] = [s.strip() for s in subtype_input.split(',')]
        
        # Provenance section
        provenance = {}
        
        # TSN
        existing_tsn = None
        if existing_metadata and 'provenance' in existing_metadata:
            existing_tsn = existing_metadata['provenance'].get('tsn')
        
        if existing_tsn:
            tsn = input(f"TSN [{existing_tsn}] (press Enter to keep): ").strip() or existing_tsn
        else:
            generated_tsn = self.generate_tsn()
            tsn = input(f"TSN [{generated_tsn}] (auto-generated): ").strip() or generated_tsn
        provenance['tsn'] = tsn
        
        # Date (ISO-8601)
        default_date = datetime.now().strftime('%Y-%m-%d')
        date = input(f"Date (ISO-8601) [{default_date}]: ").strip() or default_date
        provenance['date'] = date
        
        # Version (SemVer)
        default_version = 'v1.0.0'
        if existing_metadata and 'provenance' in existing_metadata:
            default_version = existing_metadata['provenance'].get('version', 'v1.0.0')
        version = input(f"Version (SemVer) [{default_version}]: ").strip() or default_version
        provenance['version'] = version
        
        self.metadata['provenance'] = provenance
        
        # Artifact metadata section
        artifact_metadata = {}
        
        source = input("\nSource (e.g., 'Evergy', 'Copilot'): ").strip()
        if source:
            artifact_metadata['source'] = source
        
        print("\nPurpose (one per line, empty line to finish):")
        purposes = []
        while True:
            purpose = input("  - ").strip()
            if not purpose:
                break
            purposes.append(purpose)
        if purposes:
            artifact_metadata['purpose'] = purposes
        
        filing_path = input("\nFiling path: ").strip()
        if filing_path:
            artifact_metadata['filing_path'] = filing_path
        
        # Retention class
        print(f"\nRetention classes: {', '.join(self.RETENTION_CLASSES)}")
        retention = input("Retention class [preserved]: ").strip() or 'preserved'
        artifact_metadata['retention_class'] = retention
        
        self.metadata['artifact_metadata'] = artifact_metadata
        
        # Cross-references
        cross_refs = {}
        github_issues = input("\nGitHub issue numbers (comma-separated): ").strip()
        if github_issues:
            issue_list = []
            for n in github_issues.split(','):
                n = n.strip()
                if n.isdigit():
                    issue_list.append(int(n))
                else:
                    print(f"Warning: '{n}' is not a valid issue number, skipping.")
            if issue_list:
                cross_refs['github_issues'] = issue_list
        
        onedrive_ids = input("OneDrive file IDs (comma-separated): ").strip()
        if onedrive_ids:
            cross_refs['onedrive_ids'] = [id.strip() for id in onedrive_ids.split(',')]
        
        redorepo_refs = input("REDOREPO references (comma-separated): ").strip()
        if redorepo_refs:
            cross_refs['redorepo_refs'] = [ref.strip() for ref in redorepo_refs.split(',')]
        
        if cross_refs:
            self.metadata['cross_references'] = cross_refs
        
        # Governance
        governance = {}
        sensitive = input("\nContains sensitive data? (y/n) [n]: ").strip().lower()
        governance['sensitive_data'] = sensitive == 'y'
        
        gitignore = input("Enforce .gitignore? (y/n) [y]: ").strip().lower()
        governance['gitignore_enforced'] = gitignore != 'n'
        
        encryption = input("Encryption required? (y/n) [n]: ").strip().lower()
        governance['encryption_required'] = encryption == 'y'
        
        self.metadata['governance'] = governance
        
        # Footer stamp (auto-generated)
        footer = f"DOCSYS | {system} | {artifact_type} | TSN:{tsn}"
        self.metadata['footer_stamp'] = footer
        
        # Narrative context
        print("\nNarrative context (multi-line, Ctrl+D or Ctrl+Z to finish):")
        narrative_lines = []
        try:
            while True:
                line = input()
                narrative_lines.append(line)
        except EOFError:
            pass
        
        if narrative_lines:
            self.metadata['narrative_context'] = '\n'.join(narrative_lines)
    
    def prompt_metadata_fields(self, existing_metadata=None):
        """Interactively prompt for metadata fields (simple mode)"""
        print("\n" + "=" * 70)
        print("SIMPLE METADATA FIELDS")
        print("=" * 70)
        
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
        if self.mode == 'docsys':
            # Generate full YAML dump for DOCSYS mode
            yaml_str = yaml.dump(self.metadata, default_flow_style=False, sort_keys=False, allow_unicode=True)
            return '---\n' + yaml_str + '---'
        else:
            # Simple key:value format for simple mode
            yaml_lines = ['---']
            for key, value in self.metadata.items():
                yaml_lines.append(f"{key}: {value}")
            yaml_lines.append('---')
            return '\n'.join(yaml_lines)
    
    def preview_metadata(self):
        """Display preview of metadata"""
        print("\n" + "=" * 70)
        print("METADATA PREVIEW")
        print("=" * 70)
        print("\n" + self.generate_yaml_header())
        
        if self.mode == 'docsys' and 'footer_stamp' in self.metadata:
            print("\n" + "=" * 70)
            print("FOOTER STAMP")
            print("=" * 70)
            print(f"\n{self.metadata['footer_stamp']}")
        print()
    
    def export_metadata(self, file_path):
        """Export metadata to separate files"""
        base_path = file_path.parent / (file_path.stem + '_metadata')
        
        # Export as YAML
        yaml_path = base_path.with_suffix('.yaml')
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.metadata, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"✓ YAML metadata exported: {yaml_path}")
        
        # Export as plain text
        txt_path = base_path.with_suffix('.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            if self.mode == 'docsys':
                f.write("DOCSYS Metadata Export\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"System: {self.metadata.get('system', 'N/A')}\n")
                f.write(f"Cycle: {self.metadata.get('cycle', 'N/A')}\n")
                f.write(f"Artifact Type: {self.metadata.get('artifact_type', 'N/A')}\n")
                if 'provenance' in self.metadata:
                    f.write(f"TSN: {self.metadata['provenance'].get('tsn', 'N/A')}\n")
                    f.write(f"Date: {self.metadata['provenance'].get('date', 'N/A')}\n")
                    f.write(f"Version: {self.metadata['provenance'].get('version', 'N/A')}\n")
                f.write("\n")
                if 'footer_stamp' in self.metadata:
                    f.write("Footer Stamp:\n")
                    f.write(self.metadata['footer_stamp'] + "\n")
            else:
                for key, value in self.metadata.items():
                    f.write(f"{key}: {value}\n")
        print(f"✓ Plain text metadata exported: {txt_path}")
        
        # Export as Markdown if in DOCSYS mode
        if self.mode == 'docsys':
            md_path = base_path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write("# DOCSYS Intake Overlay\n\n")
                f.write(f"**System:** {self.metadata.get('system', 'N/A')}  \n")
                f.write(f"**Cycle:** {self.metadata.get('cycle', 'N/A')}  \n")
                f.write(f"**Artifact Type:** {self.metadata.get('artifact_type', 'N/A')}  \n")
                if 'provenance' in self.metadata:
                    f.write(f"**TSN:** {self.metadata['provenance'].get('tsn', 'N/A')}  \n")
                    f.write(f"**Date:** {self.metadata['provenance'].get('date', 'N/A')}  \n")
                    f.write(f"**Version:** {self.metadata['provenance'].get('version', 'N/A')}  \n")
                f.write("\n")
                if 'artifact_metadata' in self.metadata and 'source' in self.metadata['artifact_metadata']:
                    f.write(f"**Source:** {self.metadata['artifact_metadata']['source']}  \n")
                if 'artifact_metadata' in self.metadata and 'filing_path' in self.metadata['artifact_metadata']:
                    f.write(f"**Filing Path:** `{self.metadata['artifact_metadata']['filing_path']}`  \n")
                f.write("\n---\n\n")
                if 'footer_stamp' in self.metadata:
                    f.write(f"**Footer Stamp:**  \n`{self.metadata['footer_stamp']}`\n")
            print(f"✓ Markdown overlay exported: {md_path}")
    
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
        
        # Select mode
        self.select_mode()
        print(f"\n✓ Selected mode: {self.mode.upper()}\n")
        
        # Get file path
        file_path, content = self.get_file_path()
        
        # Parse existing metadata if any
        existing_metadata, body_content = self.parse_existing_metadata(content) if content else (None, None)
        
        if existing_metadata:
            print(f"\n✓ Found existing metadata in file")
        
        # Prompt for metadata based on mode
        if self.mode == 'docsys':
            self.prompt_docsys_metadata(existing_metadata)
        else:
            self.prompt_metadata_fields(existing_metadata)
        
        # Preview
        self.preview_metadata()
        
        # Ask about export
        export_choice = input("Export metadata to separate files (YAML/TXT/MD)? (y/n): ").strip().lower()
        if export_choice == 'y':
            self.export_metadata(file_path)
        
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
