# infrastructure_health_monitor
# Author: Ali Haider   
# Date: 2024-06-15

''' Scenario
    Imagine you're a Junior DevOps Engineer.
    Your team has 10 Linux servers.
    Your task is to write a Python automation script that checks each server and generates a health report.'''

import platform
import os
from datetime import date, datetime, time

print("=" * 50)
print("      DevOps Infrastructure Health Monitor")
print("=" * 50)

print(f"Current Date     : {date.today()}")
print(f"Current Time     : {datetime.now().strftime('%H:%M:%S')}")
print(f"Python Version   : {platform.python_version()}")
print(f"Operating System : {platform.system()} {platform.release()}")

server_list = ["server1", "server2", "server3", "server4", "server5", "server6", "server7", "server8", "server9", "server10"]

for i, server in enumerate(server_list, start=1):
    print(f"\nServer {i}: {server}")

server1 = {
    "hostname": "server1", 
    "ip_address": "192.168.1.10",
    "environment": "production",
    "disk_space": "80",
}
server2 = {
    "hostname": "server2",
    "ip_address": "192.168.1.11",
    "environment": "production",
    "disk_space": "75"
}
server3 = {
    "hostname": "server3",
    "ip_address": "192.168.1.12",
    "environment": "production",
    "disk_space": "70"
}
server4 = {
    "hostname": "server4",
    "ip_address": "192.168.1.13",
    "environment": "production",
    "disk_space": "65"
}
server5 = {
    "hostname": "server5",
    "ip_address": "192.168.1.14",
    "environment": "production",
    "disk_space": "60"
}
server6 = {
    "hostname": "server6",
    "ip_address": "192.168.1.15",
    "environment": "production",
    "disk_space": "55"
}
server7 = {
    "hostname": "server7",
    "ip_address": "192.168.1.16",
    "environment": "production",
    "disk_space": "50"
}
server8 = {
    "hostname": "server8",
    "ip_address": "192.168.1.17",
    "environment": "production",
    "disk_space": "45"
}
server9 = {
    "hostname": "server9",
    "ip_address": "192.168.1.18",
    "environment": "production",
    "disk_space": "40"
}
server10 = {
    "hostname": "server10",
    "ip_address": "192.168.1.19",
    "environment": "production",
    "disk_space": "35"
}

disk_space = ["85", "75", "70", "65", "60", "55", "50", "45", "40", "35"]

if disk_space[0] in range(0, 70):
    print("Disk Space Status: Healthy")
elif disk_space[0] in range(70, 79):
    print("Disk Space Status: Warning")
elif disk_space[0] in range(80, 100):
    print("Disk Space Status: Critical")
else:
    print("Invalid disk space value. Please check the input.")



