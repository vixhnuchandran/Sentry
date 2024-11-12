import logging
from sentry.config import ALERT_THRESHOLD, LOG_FILE_PATH
from sentry.utils import read_log_file, parse_log_line

logging.basicConfig(level=logging.INFO)

failed_login_attempts = 0

def check_for_intrusion(parsed_data):
    global failed_login_attempts

    if parsed_data['log_level'] == 'ERROR' and 'failed login' in parsed_data['message'].lower():
        failed_login_attempts +=1

        if failed_login_attempts >= ALERT_THRESHOLD:
            alert_admin(parsed_data)

def alert_admin(parsed_data):
    print(f"ALERT: Too many failed login attempts! Last failed attempt: {parsed_data['message']} at {parsed_data['timestamp']}")
    global failed_login_attempts
    failed_login_attempts = 0


def process_log_data(log_file_path):
    global failed_login_attempts

    log_data = read_log_file(log_file_path)

    if not log_data:
        print("Error: No data read from the log file.")
        return

    for parsed_data in log_data:
        if parsed_data:
            check_for_intrusion(parsed_data)


def run_sentry():
    logging.info("Sentry Intrusion Detection System is starting...")
    log_file_path = LOG_FILE_PATH
    process_log_data(log_file_path)
    logging.info("Sentry Intrusion Detection System finished processing.")


if __name__ == "__main__":
    logging.info("==== Starting Sentry System ====")
    try:
        run_sentry()
        logging.info("==== Sentry System Completed Successfully ====")
    except Exception as e:
        logging.error(f"Error encountered: {str(e)}")