import os
import re
import yaml
from datetime import datetime
from pathlib import Path
import shutil  # For file operations
import time  # For timestamp

class WorkCapAnalyzer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.standard_values = {
            'credit_cards': {
                'CR MCC': 450.11,
                'CR VFB': 579.39
            },
            'buffer_minimum': 110,
            'income_range': (685, 740)
        }
        
    def archive_existing_reports(self, report_path):
        """Archive existing reports from the same day"""
        if not report_path.exists():
            return
            
        # Create archive folder if it doesn't exist
        archive_folder = report_path.parent / 'archive'
        archive_folder.mkdir(parents=True, exist_ok=True)
        
        # Get timestamp for uniqueness
        timestamp = time.strftime('%H%M%S')
        
        # Create archive filename with timestamp
        archive_name = f"{report_path.stem}_{timestamp}{report_path.suffix}"
        archive_path = archive_folder / archive_name
        
        # Move existing report to archive
        shutil.move(str(report_path), str(archive_path))

    def validate_file_structure(self, file_path):
        """Validate file naming and structure"""
        filename = Path(file_path).name
        if 'reviews' in str(file_path):
            # Check review file naming pattern
            pattern = r'\d{4}-\d{2}-\d{2}_[a-z]+\.md'
            return bool(re.match(pattern, filename))
        return True

    def parse_yaml_header(self, content):
        """Parse YAML header from markdown files"""
        if content.startswith('---'):
            try:
                end = content.index('---', 3)
                header = content[3:end]
                return yaml.safe_load(header)
            except:
                return None
        return None

    def check_file_status(self, header):
        """Validate file status"""
        valid_statuses = ['report', 'template', 'protocol', 'active']
        if header and 'file_status' in header:
            return header['file_status'] in valid_statuses
        return False

    def extract_metrics(self, content):
        """Extract key financial metrics from content"""
        metrics = {
            'buffer': None,
            'credit_usage': None,
            'debt_total': None
        }
        
        # Look for metrics in tables
        table_pattern = r'\|\s*Buffer\s*\|\s*\$?([\d.]+)\s*\|'
        credit_pattern = r'\|\s*Credit Usage\s*\|\s*([\d.]+)%\s*\|'
        debt_pattern = r'\|\s*Debt Total\s*\|\s*\$?([\d.]+)\s*\|'
        
        if match := re.search(table_pattern, content):
            metrics['buffer'] = float(match.group(1))
        if match := re.search(credit_pattern, content):
            metrics['credit_usage'] = float(match.group(1))
        if match := re.search(debt_pattern, content):
            metrics['debt_total'] = float(match.group(1))
            
        return metrics

    def validate_cross_references(self, content):
        """Validate cross-references in content"""
        ref_pattern = r'\[See:\s+([^\]]+)\]'
        references = re.findall(ref_pattern, content)
        invalid_refs = []
        
        for ref in references:
            ref_path = self.base_path / ref
            if not ref_path.exists():
                invalid_refs.append(ref)
                
        return invalid_refs

    def analyze_file(self, file_path):
        """Analyze a single file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        results = {
            'file': str(file_path),
            'structure_valid': self.validate_file_structure(file_path),
            'status_valid': False,
            'metrics': None,
            'invalid_references': [],
            'warnings': []
        }
        
        # Parse header
        header = self.parse_yaml_header(content)
        if header:
            results['status_valid'] = self.check_file_status(header)
            
            # Check last_updated date
            if 'last_updated' in header:
                try:
                    last_updated = datetime.strptime(header['last_updated'], '%Y-%m-%d')
                    if (datetime.now() - last_updated).days > 30:
                        results['warnings'].append('File not updated in over 30 days')
                except:
                    results['warnings'].append('Invalid last_updated date format')
        
        # Extract metrics if it's a review file
        if 'reviews' in str(file_path):
            results['metrics'] = self.extract_metrics(content)
            
            # Validate metrics against standards
            if results['metrics']['buffer'] is not None and results['metrics']['buffer'] < self.standard_values['buffer_minimum']:
                results['warnings'].append(f'Buffer below minimum: ${results["metrics"]["buffer"]} < ${self.standard_values["buffer_minimum"]}')
        
        # Check cross-references
        results['invalid_references'] = self.validate_cross_references(content)
        
        return results

    def analyze_workspace(self):
        """Analyze entire workspace"""
        all_results = []
        
        for root, _, files in os.walk(self.base_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    results = self.analyze_file(file_path)
                    all_results.append(results)
                    
        return self.generate_report(all_results)

    def generate_report(self, results):
        """Generate analysis report"""
        current_date = datetime.now().strftime('%Y-%m-%d')
        report = f"""---
last_updated: {current_date}
version: 1.0.0
file_status: report
---

# WorkCap Analysis Report

## Summary
Total files analyzed: {len(results)}
Files with warnings: {sum(1 for r in results if r['warnings'])}
Files with invalid references: {sum(1 for r in results if r['invalid_references'])}

## File Structure Issues
"""
        structure_issues = [r for r in results if not r['structure_valid']]
        if structure_issues:
            for issue in structure_issues:
                report += f"- Invalid structure: {issue['file']}\n"
        else:
            report += "No file structure issues found.\n"

        report += "\n## Invalid References\n"
        ref_issues = [r for r in results if r['invalid_references']]
        if ref_issues:
            for issue in ref_issues:
                report += f"File: {issue['file']}\n"
                for ref in issue['invalid_references']:
                    report += f"- Missing reference: {ref}\n"
        else:
            report += "No invalid references found.\n"

        report += "\n## Metrics Analysis\n"
        metrics_files = [r for r in results if r['metrics']]
        if metrics_files:
            for m in metrics_files:
                if m['metrics']['buffer'] is not None:
                    report += f"File: {m['file']}\n"
                    report += f"- Buffer: ${m['metrics']['buffer']}\n"
                    report += f"- Credit Usage: {m['metrics']['credit_usage']}%\n"
                    report += f"- Debt Total: ${m['metrics']['debt_total']}\n"
                    if m['warnings']:
                        report += "Warnings:\n"
                        for warning in m['warnings']:
                            report += f"- {warning}\n"
                    report += "\n"

        return report

if __name__ == '__main__':
    import argparse
    
    # Get the repository root (two directories up from this script's location)
    script_dir = Path(__file__).resolve().parent
    default_base_path = script_dir.parent.parent
    
    parser = argparse.ArgumentParser(description='Analyze WorkCap workspace')
    parser.add_argument('--base-path', type=str, default=str(default_base_path),
                        help='Base path for workspace (defaults to repository root)')
    args = parser.parse_args()
    
    analyzer = WorkCapAnalyzer(args.base_path)
    report = analyzer.analyze_workspace()
    
    # Set up report path with current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    report_path = Path(analyzer.base_path) / 'reports' / 'analysis' / f'{current_date}_workcap_analysis.md'
    
    # Archive existing report if it exists
    analyzer.archive_existing_reports(report_path)
    
    # Ensure directory exists and save new report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Report generated: {report_path}")
