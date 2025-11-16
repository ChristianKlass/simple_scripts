# Keep Awake

Prevents screen timeout by simulating minimal mouse movement - perfect for screen recordings, presentations, or long-running tasks.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Run indefinitely (stop with Ctrl+C)
./keep_awake.py

# Move mouse every 30 seconds
./keep_awake.py -i 30

# Run for 2 hours
./keep_awake.py -d 120

# Move every 45 seconds for 90 minutes
./keep_awake.py -i 45 -d 90
```

## Options

- `-i, --interval SECONDS` - Seconds between mouse movements (default: 60)
- `-d, --duration MINUTES` - Total duration in minutes (default: run until stopped)
- `-h, --help` - Show help message

## How It Works

The script moves the mouse cursor by 1 pixel and immediately back to its original position. This minimal movement:

- Prevents screen timeout/sleep
- Is virtually invisible during recordings
- Doesn't interfere with your work
- Can run in the background

## Use Cases

- Recording coding sessions or tutorials
- Presentations or demos
- Monitoring dashboards
- Long-running processes that need the screen active

## Requirements

- Python 3.6+
- pyautogui

## Safety

The script includes `FAILSAFE=True`, which means you can stop it by moving your mouse to any screen corner in case of issues.
