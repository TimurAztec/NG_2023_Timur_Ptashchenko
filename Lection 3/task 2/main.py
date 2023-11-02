import json
import platform
import socket
import os
import psutil

system_info = {
    "OS": platform.system(),
    "OS Version": platform.uname().release,
    "Machine": platform.machine(),
    "CPU": platform.processor(),
    "Hostname": socket.gethostname(),
    "IP Address": socket.gethostbyname(socket.gethostname()),
    "CPU Cores": os.cpu_count(),
    "Total Memory": psutil.virtual_memory().total,
}

print(json.dumps(system_info, indent=4))