# Sentry IDS

Sentry is an Intrusion Detection System that monitors server logs for failed login attempts and alerts administrators about potential threats.

## Features

- **Log Parsing**: Reads and analyzes server logs.
- **Intrusion Detection**: Detects failed login attempts.
- **Alert System**: Sends notifications when a threshold is exceeded.

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/vixhnuchandran/Sentry.git
    cd Sentry
    ```

2. (Optional) Install the project locally:

    ```bash
    pip install -e .
    ```

## Configuration

Modify `Sentry/config.py`:

- **LOG_FILE_PATH**: Log file path (default: `server_log.txt`).
- **ALERT_THRESHOLD**: Alert threshold for failed logins (default: `5`).

## Usage

Run the IDS:

```bash
python run_sentry.py
