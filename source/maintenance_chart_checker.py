"""Maintenance Chart Checker

This script analyzes maintenance charts in reStructuredText (.rst) files. It recursively scans
through directories looking for .rst files containing maintenance charts in the format:

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-04-13   | reviewer                      | Release        | Pass/Fail                      |
+--------------+-------------------------------+----------------+--------------------------------+

The script generates a summary report showing:
- Total number of files with maintenance charts in each directory
- Number of empty maintenance charts
- Number of charts with passing test situations
- Number of charts with failing test situations

Usage:
    # Run from current directory (default depth=1)
    python maintenance_chart_checker.py
    
    # Run from specific directory with custom depth
    python maintenance_chart_checker.py path/to/docs --depth 2
    
    # Show full directory paths (depth=0)
    python maintenance_chart_checker.py --depth 0
    
    # Show help
    python maintenance_chart_checker.py -h

Example output with depth=1:
------------------------------------------------------------
| Folder               |   Total |   Empty |  Passed |  Failed |
------------------------------------------------------------
| educators            |      12 |       3 |       5 |       4 |
| faculty             |       8 |       1 |       4 |       3 |
------------------------------------------------------------

Example output with depth=2:
------------------------------------------------------------
| Folder               |   Total |   Empty |  Passed |  Failed |
------------------------------------------------------------
| educators/how-tos    |       8 |       2 |       4 |       2 |
| educators/reference  |       4 |       1 |       1 |       2 |
| faculty/guides      |       8 |       1 |       4 |       3 |
------------------------------------------------------------
"""

import os
import argparse
from typing import Dict, List, NamedTuple
from collections import defaultdict

class MaintenanceStatus(NamedTuple):
    is_empty: bool
    has_fail: bool
    has_pass: bool
    file_path: str

def parse_maintenance_chart(content: str) -> MaintenanceStatus | None:
    """Parse the maintenance chart in the content and return its status."""
    # Check if maintenance chart exists
    if "**Maintenance chart**" not in content:
        return None
    
    # Split content into lines and find the maintenance chart section
    lines = content.split('\n')
    try:
        chart_start = next(i for i, line in enumerate(lines) if "**Maintenance chart**" in line)
    except StopIteration:
        return None
    
    # Find both header separator lines
    try:
        separators = [i for i in range(chart_start, len(lines)) 
                     if '+-' in lines[i] and '-+' in lines[i]]
        if len(separators) < 2:  # Need both top and bottom separator
            return None
        first_data_idx = separators[1] + 1  # Take the line after the second separator
    except (StopIteration, IndexError):
        return None
    
    # Get the first data row
    if first_data_idx >= len(lines):
        return None
    
    first_data_row = lines[first_data_idx].strip()
    
    # Check if the row is empty (just separators and spaces)
    is_empty = all(cell.strip() in ['|', '', ' '] for cell in first_data_row.split('|'))
    
    # Look for pass/fail in test situation column (last column)
    columns = [col.strip().lower() for col in first_data_row.split('|') if col.strip()]
    if not columns:  # Empty row
        return MaintenanceStatus(True, False, False, "")
        
    # The test situation is in the last column
    test_situation = columns[-1] if len(columns) >= 4 else ""
    has_fail = 'fail' in test_situation.lower()
    has_pass = 'pass' in test_situation.lower()
    
    return MaintenanceStatus(is_empty, has_fail, has_pass, "")

def get_folder_path(path: str, start_path: str, depth: int) -> str:
    """Get the directory path at specified depth relative to start_path."""
    rel_path = os.path.relpath(path, start_path)
    if depth == 0:
        return rel_path
    parts = rel_path.split(os.sep)
    return os.sep.join(parts[:depth]) if depth < len(parts) else rel_path

def scan_directory(start_path: str, depth: int) -> Dict[str, List[MaintenanceStatus]]:
    """Recursively scan directory for .rst files and analyze maintenance charts."""
    results = defaultdict(list)
    
    for root, _, files in os.walk(start_path):
        rst_files = [f for f in files if f.endswith('.rst')]
        if not rst_files:
            continue
            
        for file in rst_files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                status = parse_maintenance_chart(content)
                if status is not None:  # Only include files with maintenance charts
                    folder_path = get_folder_path(root, start_path, depth)
                    results[folder_path].append(MaintenanceStatus(
                        status.is_empty,
                        status.has_fail,
                        status.has_pass,
                        file_path
                    ))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                
    return results

def print_report(results: Dict[str, List[MaintenanceStatus]]):
    """Print a formatted report table of the maintenance chart analysis."""
    print("\nMaintenance Chart Analysis Report")
    print("================================\n")
    
    # Print table header
    header = "| {:<30} | {:>8} | {:>8} | {:>8} | {:>8} |".format(
        "Folder", "Total", "Empty", "Passed", "Failed"
    )
    separator = "-" * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    # Print table rows
    for folder, statuses in sorted(results.items()):
        total = len(statuses)
        empty = sum(1 for s in statuses if s.is_empty)
        passed = sum(1 for s in statuses if s.has_pass)
        failed = sum(1 for s in statuses if s.has_fail)
        
        row = "| {:<30} | {:>8} | {:>8} | {:>8} | {:>8} |".format(
            folder, total, empty, passed, failed
        )
        print(row)
    
    print(separator)

def main():
    parser = argparse.ArgumentParser(
        description='Analyze maintenance charts in .rst files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s                     # Run from current directory (depth=1)
    %(prog)s path/to/docs        # Run from specified directory
    %(prog)s --depth 2           # Group by two directory levels
    %(prog)s --depth 0           # Show full directory paths
    %(prog)s -h                  # Show this help message
        """
    )
    
    parser.add_argument(
        'start_dir',
        nargs='?',
        default='.',
        help='Directory to start scanning from (default: current directory)'
    )
    
    parser.add_argument(
        '--depth', '-d',
        type=int,
        default=1,
        help='Number of directory levels to show in report (0 for full path, default: 1)'
    )

    args = parser.parse_args()
    
    # Convert to absolute path and verify directory exists
    start_path = os.path.abspath(args.start_dir)
    if not os.path.isdir(start_path):
        print(f"Error: Directory '{args.start_dir}' does not exist")
        return
        
    results = scan_directory(start_path, args.depth)
    print_report(results)

if __name__ == "__main__":
    main() 