"""Maintenance Chart Checker

This script analyzes maintenance charts in reStructuredText (.rst) files. It recursively scans
through directories looking for .rst files containing maintenance charts in the format:

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-04-13   | reviewer                      | Release        | Pass/Fail/Deprecated           |
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

from docutils.core import publish_doctree
import docutils.nodes as nodes

class MaintenanceStatus(NamedTuple):
    is_empty: bool
    has_fail: bool
    has_pass: bool
    has_deprecated: bool
    file_path: str

def _truncate_at_next_section(all_lines: list, start_index: int) -> list:
    """Return lines from start_index up to (not including) the next section header or include directive.

    This keeps the excerpt small so docutils never processes directives like
    ``.. include::`` that require the full Sphinx build environment.

    RST section adornments are lines where the same non-word character is
    repeated three or more times, e.g.:
      =========   (title overline/underline)
      ---------   (section underline)
      #########   (chapter overline/underline)
    Table borders like ``+-----+`` are not matched because they contain mixed characters.
    """
    import re
    # Matches a line consisting entirely of 3+ repetitions of the same punctuation char.
    # Examples that match:  ===  ---  ###  ~~~  ***
    # Examples that do not: +-+  .. include::  | cell |
    section_adornment = re.compile(r'^([^\w\s])\1{2,}\s*$')
    # Seed the list with the marker line itself, then scan forward from the next line.
    # The stop-check runs only on subsequent lines so the marker is never accidentally
    # matched against the adornment pattern.
    excerpt_lines = [all_lines[start_index]]
    for line in all_lines[start_index + 1:]:
        if line.startswith('.. include::') or section_adornment.match(line):
            break
        excerpt_lines.append(line)
    return excerpt_lines


def parse_maintenance_chart(content: str) -> MaintenanceStatus | None:
    """Parse the maintenance chart using docutils; supports grid tables and list-tables.

    Only the excerpt starting at the **Maintenance chart** marker is parsed so
    that full-document parsing overhead is avoided.
    """
    if "**Maintenance chart**" not in content:
        return None

    all_lines = content.split('\n')
    try:
        chart_start_index = next(
            index for index, line in enumerate(all_lines)
            if "**Maintenance chart**" in line
        )
    except StopIteration:
        return None

    chart_excerpt = '\n'.join(_truncate_at_next_section(all_lines, chart_start_index))
    doctree = publish_doctree(chart_excerpt, settings_overrides={'report_level': 5})

    all_tables = list(doctree.findall(nodes.table))
    if not all_tables:
        return None

    maintenance_table = all_tables[0]

    # list-table (and grid tables using = header separator) populate table_header;
    # plain grid tables with only - separators put all rows in table_body.
    table_header = maintenance_table.next_node(nodes.thead)
    table_body = maintenance_table.next_node(nodes.tbody)
    if table_body is None:
        return None

    all_body_rows = list(table_body.children)
    # When there is no table_header the first row in all_body_rows is the column-header row; skip it.
    data_rows = all_body_rows if table_header is not None else all_body_rows[1:]

    if not data_rows:
        return MaintenanceStatus(True, False, False, False, "")

    first_data_row_cells = list(data_rows[0].findall(nodes.entry))
    if not first_data_row_cells:
        return MaintenanceStatus(True, False, False, False, "")

    test_situation = first_data_row_cells[-1].astext().strip().lower()
    is_empty = not test_situation
    return MaintenanceStatus(
        is_empty,
        'fail' in test_situation,
        'pass' in test_situation,
        'deprecated' in test_situation,
        "",
    )


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
                        status.has_deprecated,
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
    header = "| {:<30} | {:>8} | {:>8} | {:>8} | {:>8} | {:>10} |".format(
        "Folder", "Total", "Empty", "Passed", "Failed", "Deprecated"
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
        deprecated = sum(1 for s in statuses if s.has_deprecated)
        
        row = "| {:<30} | {:>8} | {:>8} | {:>8} | {:>8} | {:>10} |".format(
            folder, total, empty, passed, failed, deprecated
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