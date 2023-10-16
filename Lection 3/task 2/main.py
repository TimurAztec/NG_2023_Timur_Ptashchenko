import json
import psutil
import platform
import socket

system_info = {
    "OS": platform.system(),
    "OS Version": platform.version(),
    "Machine": platform.machine(),
    "CPU": platform.processor(),
    "Hostname": socket.gethostname(),
    "IP Address": socket.gethostbyname(socket.gethostname()),
    "CPU Cores": psutil.cpu_count(logical=False),
    "CPU Usage": psutil.cpu_percent(interval=1, percpu=True),
    "Total Memory": psutil.virtual_memory().total,
    "Available Memory": psutil.virtual_memory().available
}

print(json.dumps(system_info, indent=4))