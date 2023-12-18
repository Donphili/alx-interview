#!/usr/bin/python3
"""Log Parser"""

import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Process stdin line by line
for line in sys.stdin:
    try:
        # Parse the line
        _, _, _, _, _, status_code_str, file_size_str = line.split(" ")
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        
        # Update metrics
        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except ValueError:
        # Skip lines with incorrect format
        pass
