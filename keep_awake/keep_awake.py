#!/usr/bin/env python3
"""
Keep Awake Script
Prevents screen timeout during screen recordings or presentations
by simulating minimal mouse movement.
"""

import pyautogui
import time
import argparse
import sys

def keep_awake(interval=60, duration=None):
    """
    Simulate small mouse movements to prevent screen timeout.

    Args:
        interval: Seconds between mouse movements (default: 60)
        duration: Total duration in minutes (None = run until Ctrl+C)
    """
    print("Keep Awake Script Started")
    print(f"Moving mouse every {interval} seconds")
    if duration:
        print(f"Will run for {duration} minutes")
    else:
        print("Press Ctrl+C to stop")
    print("-" * 40)

    # Disable pyautogui failsafe for smoother operation
    pyautogui.FAILSAFE = True

    start_time = time.time()
    end_time = start_time + (duration * 60) if duration else None
    move_count = 0

    try:
        while True:
            # Check if we've reached the duration limit
            if end_time and time.time() >= end_time:
                print("\nDuration reached. Stopping...")
                break

            # Get current mouse position
            current_x, current_y = pyautogui.position()

            # Move mouse slightly (1 pixel) and back
            pyautogui.moveRel(1, 0, duration=0.1)
            pyautogui.moveRel(-1, 0, duration=0.1)

            move_count += 1
            elapsed = int(time.time() - start_time)
            print(f"Movement #{move_count} at {elapsed}s - Position: ({current_x}, {current_y})", end='\r')

            # Wait for the specified interval
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n\nStopped by user")
        print(f"Total movements: {move_count}")
        print(f"Total time: {int(time.time() - start_time)} seconds")
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Prevent screen timeout by simulating mouse movement',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run indefinitely with 60s interval
  %(prog)s -i 30              # Move every 30 seconds
  %(prog)s -d 120             # Run for 120 minutes
  %(prog)s -i 45 -d 90        # Move every 45s for 90 minutes
        """
    )

    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=60,
        help='Seconds between mouse movements (default: 60)'
    )

    parser.add_argument(
        '-d', '--duration',
        type=int,
        default=None,
        help='Total duration in minutes (default: run until stopped)'
    )

    args = parser.parse_args()

    # Validate arguments
    if args.interval < 1:
        print("Error: Interval must be at least 1 second", file=sys.stderr)
        sys.exit(1)

    if args.duration is not None and args.duration < 1:
        print("Error: Duration must be at least 1 minute", file=sys.stderr)
        sys.exit(1)

    keep_awake(interval=args.interval, duration=args.duration)

if __name__ == '__main__':
    main()
