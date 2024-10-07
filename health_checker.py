import requests
import time
import datetime

# Application URL
APP_URL = 'http://your-application-url.com'  # Replace with the URL of your application

# Log file for uptime checks
LOG_FILE = 'uptime_log.txt'

# Time interval between checks (in seconds)
CHECK_INTERVAL = 60  # e.g., check every 60 seconds

def log_message(message):
    """ Log messages with timestamps """
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")
    print(message)

def check_uptime():
    """ Check the application status """
    try:
        # Send a GET request to the application
        response = requests.get(APP_URL, timeout=5)
        
        # Check if the application is 'up' based on the status code
        if response.status_code >= 200 and response.status_code < 300:
            log_message(f"Application is UP. Status Code: {response.status_code}")
        else:
            log_message(f"Application is DOWN. Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # If there is a connection issue or timeout, consider the app 'down'
        log_message(f"Application is DOWN. Error: {str(e)}")

# Run the uptime check in a loop
while True:
    check_uptime()
    time.sleep(CHECK_INTERVAL)
