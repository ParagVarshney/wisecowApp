import psutil
import datetime

# Define threshold values
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Log file
LOG_FILE = "system_health.log"

def log_message(message):
    """ Log messages with timestamp """
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")
    print(message)

def check_cpu():
    """ Check CPU usage """
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"CPU usage is above threshold: {cpu_usage}%")
    else:
        log_message(f"CPU usage is normal: {cpu_usage}%")

def check_memory():
    """ Check memory usage """
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"Memory usage is above threshold: {memory_usage}%")
    else:
        log_message(f"Memory usage is normal: {memory_usage}%")

def check_disk():
    """ Check disk usage """
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"Disk usage is above threshold: {disk_usage}%")
    else:
        log_message(f"Disk usage is normal: {disk_usage}%")

def check_processes():
    """ Check number of running processes """
    running_processes = len(psutil.pids())
    log_message(f"There are currently {running_processes} running processes.")

# Run the checks
check_cpu()
check_memory()
check_disk()
check_processes()
