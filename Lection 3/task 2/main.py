import json
import platform
import socket
import os

system_info = {
    "OS": platform.system(),
    "OS Version": platform.uname().release,
    "Machine": platform.machine(),
    "CPU": platform.processor(),
    "Hostname": socket.gethostname(),
    "IP Address": socket.gethostbyname(socket.gethostname()),
    "CPU Cores": os.cpu_count(),
    "Total Memory": os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'),
}

print(json.dumps(system_info, indent=4))
