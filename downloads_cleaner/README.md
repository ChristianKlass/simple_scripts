# Downloads Cleaner

Organizes your Downloads folder by automatically moving files into categorized subfolders - perfect for managing clutter from 3D printing files (STL, GCODE), documents, images, and more.

## Installation

No dependencies required - uses Python standard library only.

```bash
# Requires Python 3.6+
python --version
```

## Usage

```bash
# Preview what would happen (recommended first run)
python downloads_cleaner.py --dry-run

# Organize ~/Downloads (Windows: C:\Users\YourName\Downloads)
python downloads_cleaner.py

# Organize custom directory
python downloads_cleaner.py -d /path/to/folder

# Only organize STL files and images
python downloads_cleaner.py -c 3D_Models Images

# Only process files older than 7 days
python downloads_cleaner.py --age 7

# Combine options
python downloads_cleaner.py --dry-run --age 30 -c 3D_Models
```

On Linux/Mac with executable permissions:
```bash
./downloads_cleaner.py --dry-run
```

## Options

- `-d, --directory PATH` - Directory to organize (default: ~/Downloads)
- `--dry-run` - Preview changes without moving files
- `--age DAYS` - Only process files older than DAYS
- `-c, --categories CAT [CAT...]` - Only process specific categories
- `--list-categories` - Show all available categories and exit

## Categories

Files are organized into these subfolders:

- **3D_Models** - `.stl`, `.obj`, `.3mf`, `.amf`, `.gcode`
- **Images** - `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.ico`
- **Documents** - `.pdf`, `.doc`, `.docx`, `.txt`, `.odt`, `.rtf`, `.md`
- **Spreadsheets** - `.xls`, `.xlsx`, `.csv`, `.ods`
- **Archives** - `.zip`, `.tar`, `.gz`, `.bz2`, `.7z`, `.rar`, `.xz`
- **Videos** - `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`
- **Audio** - `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`
- **Code** - `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.sh`, `.json`, `.xml`
- **Installers** - `.exe`, `.dmg`, `.deb`, `.rpm`, `.appimage`, `.msi`
- **Other** - Everything else

## How It Works

1. Scans your Downloads folder for files (skips directories and hidden files)
2. Categorizes files by extension
3. Creates category subfolders (e.g., `~/Downloads/3D_Models/`)
4. Moves files into their respective folders
5. Handles name conflicts by adding `_1`, `_2`, etc.

## Use Cases

- **3D Printing** - Automatically organize STL/GCODE files after downloading models
- **Regular Cleanup** - Run weekly/monthly to keep Downloads organized
- **Focused Organization** - Only organize specific file types (STLs, PDFs, etc.)
- **Bulk Organization** - Clean up years of accumulated downloads

## Examples

```bash
# First time: see what would happen
python downloads_cleaner.py --dry-run

# Organize everything
python downloads_cleaner.py

# Only organize 3D printer files
python downloads_cleaner.py -c 3D_Models

# Organize old files, keep recent downloads in root
python downloads_cleaner.py --age 14

# Custom downloads location (Windows example)
python downloads_cleaner.py -d "C:\Users\Mark\Downloads"
```

## Safety Features

- **Dry-run mode** - Always preview before making changes
- **Name conflict handling** - Never overwrites existing files
- **Age filtering** - Optionally preserve recent downloads
- **Category filtering** - Only organize specific file types
- **Error reporting** - Shows which files failed to move and why

## Automation (Optional)

### Windows Task Scheduler
Run weekly to keep Downloads clean:
1. Open Task Scheduler
2. Create Basic Task → Weekly
3. Action: Start a program
4. Program: `python`
5. Arguments: `C:\path\to\downloads_cleaner.py`

### Linux/Mac Cron
```bash
# Add to crontab (crontab -e)
# Run every day at 2 AM
0 2 * * * /usr/bin/python3 /path/to/downloads_cleaner.py
```

### Shell Alias
```bash
# Add to ~/.bashrc or ~/.zshrc
alias clean-dl='python ~/simple_scripts/downloads_cleaner/downloads_cleaner.py'

# Usage: just type
clean-dl --dry-run
```
