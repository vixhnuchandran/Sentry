import re
from datetime import datetime


def read_log_file(file_path):
    parsed_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_data = parse_log_line(line.strip())
                if parsed_data:
                    parsed_lines.append(parsed_data)
    except Exception as e:
        print(f"Error reading file: {e}")
    except FileNotFoundError:
        print(f"Error: The log file {file_path} was not found.")
    return parsed_lines

def parse_log_line(line):
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(?P<level>\w+),(?P<message>.*?)(?: from (?P<ip>[\d\.]+))?$'
    match = re.match(pattern, line)

    if match:
        timestamp = match.group('timestamp')
        log_level = match.group('level')
        message = match.group('message')
        ip = match.group('ip') if match.group('ip') else None

        try:
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print(f"Error: Invalid timestamp format in line: {line}")
            return None

        return {
            'timestamp': timestamp,
            'log_level': log_level,
            'message': message,
            'ip': ip
        }
    else:
        print(f"Warning: Could not parse line: {line}")
        return None
