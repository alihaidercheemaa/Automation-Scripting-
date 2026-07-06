# infrastructure_health_monitor
# Author: Ali Haider   
# Date: 2024-06-15

''' Scenario
    Imagine you're a Junior DevOps Engineer.
    Your team has 10 Linux servers.
    Your task is to write a Python automation script that checks each server and generates a health report.'''

import platform
from datetime import date, datetime

print("=" * 50)
print("      DevOps Infrastructure Health Monitor")
print("=" * 50)

print(f"Current Date     : {date.today()}")
print(f"Current Time     : {datetime.now().strftime('%H:%M:%S')}")
print(f"Python Version   : {platform.python_version()}")
print(f"Operating System : {platform.system()} {platform.release()}")

servers = [
    {
        "hostname": "web_app_1",
        "ip_address": "192.168.1.10",
        "environment": "production",
        "disk_space": 85
    },
    {
        "hostname": "web_app_2",
        "ip_address": "192.168.1.11",
        "environment": "production",
        "disk_space": 75
    },
    {
        "hostname": "monitoring_server_1",
        "ip_address": "192.168.1.12",
        "environment": "production",
        "disk_space": 70
    },
    {
        "hostname": "proxy_server_1",
        "ip_address": "192.168.1.13",
        "environment": "production",
        "disk_space": 65
    },
    {
        "hostname": "db_cache_1",   
        "ip_address": "192.168.1.14",
        "environment": "production",
        "disk_space": 60
    },
    {
        "hostname": "db_prod_1",
        "ip_address": "192.168.1.15",
        "environment": "production",
        "disk_space": 55
    },
    {
        "hostname": "storage_prod_1",
        "ip_address": "192.168.1.16",
        "environment": "production",
        "disk_space": 50
    },
    {
        "hostname": "worker_prod_1",
        "ip_address": "192.168.1.17",
        "environment": "production",
        "disk_space": 45
    },
    {
        "hostname": "backup_prod_1",
        "ip_address": "192.168.1.18",
        "environment": "production",
        "disk_space": 40
    },
    {
        "hostname": "backup_prod_2",
        "ip_address": "192.168.1.19",
        "environment": "production",
        "disk_space": 90
    }
]

for i, server in enumerate(servers, start=1):
    if server["disk_space"] > 0 and server["disk_space"] <= 69:
        status = "Healthy"
    elif server["disk_space"] >= 70 and server["disk_space"] <= 89:
        status = "Warning"
    elif server["disk_space"] >= 90 and server["disk_space"] <= 100:
        status = "Critical"
    print("=" * 30)
    print(f"\nServer {i}: {server['hostname']} \nDisk Space: {server['disk_space']}% \nStatus: {status}")
