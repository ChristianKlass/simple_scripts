# Simple Scripts

A collection of useful Python scripts for various automation and utility tasks.

## Repository Structure

Each script is organized in its own folder with dedicated dependencies:

```
simple_scripts/
├── keep_awake/          # Prevent screen timeout during recordings
│   ├── keep_awake.py
│   └── requirements.txt
└── [future_script]/     # Each new script gets its own folder
    ├── script.py
    └── requirements.txt
```

## Available Scripts

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

Navigate to the specific script folder and install its dependencies:

```bash
cd keep_awake
pip install -r requirements.txt
```

## Categories (Future Organization)

As the collection grows, we may organize scripts into categories:

- **automation/** - Task automation scripts
- **utilities/** - General utility tools
- **system/** - System management scripts
- **media/** - Media processing tools
- **data/** - Data processing and analysis

For now, each script lives in its own top-level folder for simplicity
