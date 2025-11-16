#!/usr/bin/env python3
"""
Downloads Cleaner Script
Organizes downloads folder by moving files into categorized subfolders.
"""

import os
import shutil
import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# File categories and their extensions
FILE_CATEGORIES = {
    '3D_Models': ['.stl', '.obj', '.3mf', '.amf', '.gcode'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf', '.md'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
    'Archives': ['.zip', '.tar', '.gz', '.bz2', '.7z', '.rar', '.xz'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.sh', '.json', '.xml'],
    'Installers': ['.exe', '.dmg', '.deb', '.rpm', '.appimage', '.msi'],
}

def get_category(file_path):
    """Determine file category based on extension."""
    ext = file_path.suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Other'

def get_file_age_days(file_path):
    """Get file age in days."""
    mtime = os.path.getmtime(file_path)
    age = datetime.now() - datetime.fromtimestamp(mtime)
    return age.days

def organize_downloads(downloads_dir, dry_run=False, min_age_days=0, categories=None):
    """
    Organize downloads folder by moving files into categorized subfolders.

    Args:
        downloads_dir: Path to downloads directory
        dry_run: If True, only show what would be done
        min_age_days: Only process files older than this many days
        categories: List of specific categories to process (None = all)
    """
    downloads_path = Path(downloads_dir).expanduser()

    if not downloads_path.exists():
        print(f"Error: Directory {downloads_path} does not exist", file=sys.stderr)
        sys.exit(1)

    if not downloads_path.is_dir():
        print(f"Error: {downloads_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Collect files to process
    files_by_category = defaultdict(list)
    total_size = 0

    for item in downloads_path.iterdir():
        # Skip directories and hidden files
        if item.is_dir() or item.name.startswith('.'):
            continue

        # Check file age
        if min_age_days > 0 and get_file_age_days(item) < min_age_days:
            continue

        category = get_category(item)

        # Filter by categories if specified
        if categories and category not in categories:
            continue

        files_by_category[category].append(item)
        total_size += item.stat().st_size

    if not files_by_category:
        print("No files to organize")
        return

    # Display summary
    print(f"Downloads Cleaner - {'DRY RUN' if dry_run else 'ACTIVE MODE'}")
    print(f"Directory: {downloads_path}")
    print("-" * 60)

    total_files = sum(len(files) for files in files_by_category.values())
    print(f"Found {total_files} files ({total_size / (1024*1024):.1f} MB)\n")

    for category in sorted(files_by_category.keys()):
        files = files_by_category[category]
        cat_size = sum(f.stat().st_size for f in files)
        print(f"{category}: {len(files)} files ({cat_size / (1024*1024):.1f} MB)")

    print()

    if dry_run:
        print("DRY RUN - No files will be moved")
        print("\nFiles to be organized:")
        for category in sorted(files_by_category.keys()):
            print(f"\n{category}/")
            for file_path in sorted(files_by_category[category]):
                age_days = get_file_age_days(file_path)
                size_mb = file_path.stat().st_size / (1024*1024)
                print(f"  - {file_path.name} ({size_mb:.2f} MB, {age_days}d old)")
        return

    # Move files
    moved_count = 0
    error_count = 0

    for category, files in files_by_category.items():
        # Create category folder
        category_dir = downloads_path / category
        category_dir.mkdir(exist_ok=True)

        for file_path in files:
            dest_path = category_dir / file_path.name

            # Handle name conflicts
            if dest_path.exists():
                base = dest_path.stem
                ext = dest_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = category_dir / f"{base}_{counter}{ext}"
                    counter += 1

            try:
                shutil.move(str(file_path), str(dest_path))
                print(f"✓ {file_path.name} → {category}/")
                moved_count += 1
            except Exception as e:
                print(f"✗ Failed to move {file_path.name}: {e}", file=sys.stderr)
                error_count += 1

    print(f"\n{'-' * 60}")
    print(f"Moved: {moved_count} files")
    if error_count > 0:
        print(f"Errors: {error_count} files")

def main():
    parser = argparse.ArgumentParser(
        description='Organize downloads folder by moving files into categorized subfolders',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Organize ~/Downloads
  %(prog)s --dry-run                    # Preview changes without moving files
  %(prog)s -d ~/Downloads --age 7       # Only files older than 7 days
  %(prog)s -c 3D_Models Images          # Only organize STL files and images
  %(prog)s -d /path/to/folder           # Custom downloads folder

Categories:
  3D_Models, Images, Documents, Spreadsheets, Archives,
  Videos, Audio, Code, Installers, Other
        """
    )

    parser.add_argument(
        '-d', '--directory',
        type=str,
        default='~/Downloads',
        help='Downloads directory to organize (default: ~/Downloads)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without moving files'
    )

    parser.add_argument(
        '--age',
        type=int,
        default=0,
        metavar='DAYS',
        help='Only process files older than DAYS (default: 0 = all files)'
    )

    parser.add_argument(
        '-c', '--categories',
        nargs='+',
        metavar='CATEGORY',
        help='Only process specific categories (e.g., 3D_Models Images)'
    )

    parser.add_argument(
        '--list-categories',
        action='store_true',
        help='List all available categories and exit'
    )

    args = parser.parse_args()

    if args.list_categories:
        print("Available categories:\n")
        for category, extensions in sorted(FILE_CATEGORIES.items()):
            print(f"{category}:")
            print(f"  {', '.join(extensions)}")
        return

    # Validate categories
    if args.categories:
        invalid = [c for c in args.categories if c not in FILE_CATEGORIES and c != 'Other']
        if invalid:
            print(f"Error: Invalid categories: {', '.join(invalid)}", file=sys.stderr)
            print(f"Use --list-categories to see available options", file=sys.stderr)
            sys.exit(1)

    # Validate age
    if args.age < 0:
        print("Error: Age must be 0 or positive", file=sys.stderr)
        sys.exit(1)

    try:
        organize_downloads(
            args.directory,
            dry_run=args.dry_run,
            min_age_days=args.age,
            categories=args.categories
        )
    except KeyboardInterrupt:
        print("\n\nStopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
