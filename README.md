# Simple Scripts

A collection of useful Python scripts for various automation and utility tasks.

## Repository Structure

Each script is organized in its own folder with dedicated dependencies:

```
simple_scripts/
├── downloads_cleaner/   # Organize downloads into categorized folders
│   ├── downloads_cleaner.py
│   └── README.md
├── keep_awake/          # Prevent screen timeout during recordings
│   ├── keep_awake.py
│   └── requirements.txt
└── [future_script]/     # Each new script gets its own folder
    ├── script.py
    └── requirements.txt
```

## Available Scripts

### downloads_cleaner
Organizes Downloads folder by moving files into categorized subfolders (3D_Models, Images, Documents, etc.) - perfect for managing STL files and download clutter.

[View documentation](downloads_cleaner/)

### keep_awake
Prevents screen timeout by simulating minimal mouse movement - perfect for screen recordings, presentations, or long-running tasks.

[View documentation](keep_awake/)

## Adding New Scripts

When adding a new script:

1. Create a dedicated folder: `mkdir my_script/`
2. Add your Python script(s)
3. Create a `requirements.txt` if you have dependencies
4. Optionally add a README.md explaining usage
5. Update this main README with a brief description

## Installation

Some scripts have no dependencies (downloads_cleaner), others require installation:

```bash
# For scripts with requirements.txt
cd keep_awake
pip install -r requirements.txt

# For scripts without dependencies (downloads_cleaner)
# Just run with python - no installation needed
```

## Categories (Future Organization)

As the collection grows, we may organize scripts into categories:

- **automation/** - Task automation scripts
- **utilities/** - General utility tools
- **system/** - System management scripts
- **media/** - Media processing tools
- **data/** - Data processing and analysis

For now, each script lives in its own top-level folder for simplicity
