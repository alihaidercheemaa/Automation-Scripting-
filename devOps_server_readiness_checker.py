# Script for checking whether the server is ready for deployment or not.
# Author : Ali Haider

from datetime import datetime

servers = [
    {
    "hostname": "web-prod-01",
    "ip_address": "192.168.10.10",
    "environment": "production",
    "cpu_usage": 45,
    "ram_usage": 62,
    "disk_usage": 55,
    "status": "Running"

    },
    {
    "hostname": "web-prod-02",
    "ip_address": "192.168.10.11",
    "environment": "production",
    "cpu_usage": 50,
    "ram_usage": 65,
    "disk_usage": 67,
    "status": "Running"
    },
    {
    "hostname": "monitoring-prod-03",
    "environment": "production",
    "cpu_usage": 95,
    "ram_usage": 83,
    "disk_usage": 91,
    "status": "stopped"
    },
    {
    "hostname": "db-prod-01",
    "environment": "production",
    "cpu_usage": 30,
    "ram_usage": 43,
    "disk_usage": 52,
    "status": "Running"
    },
    {
    "hostname": "cache-prod-01",
    "environment": "production",
    "cpu_usage": 20,
    "ram_usage": 26,
    "disk_usage": 33,
    "status": "Running"
    },
    {
    "hostname": "backup-prod-01",
    "environment": "production",
    "cpu_usage": 10,
    "ram_usage": 20,
    "disk_usage": 23,
    "status": "Running"
    },
    {
    "hostname": "backup-prod-02",
    "environment": "production",
    "cpu_usage": 15,
    "ram_usage": 25,
    "disk_usage": 28,
    "status": "Running"
    },
    {
    "hostname": "storage-prod-01",
    "environment": "production",
    "cpu_usage": 18,
    "ram_usage": 30,
    "disk_usage": 40,
    "status": "Running"
    },
    {
    "hostname": "storage-prod-02",
    "environment": "production",
    "cpu_usage": 82,
    "ram_usage": 95,
    "disk_usage": 40,
    "status": "stopped"
    }
]

ready_server = 0
stopped_server = 0
total_servers = len(servers)

for index, server in enumerate(servers, start=1):
    if server['cpu_usage'] < 80 and server['ram_usage'] < 80 and server['disk_usage'] < 80 and server['status'] == "Running":
        print("=" * 30)
        print(f"Server Number: {index}")
        print(f"Server Name:   {server['hostname']}")
        print(f"environment:   {server['environment']}")
        print(f"CPU Usage:     {server['cpu_usage']}%")
        print(f"RAM Usage:     {server['ram_usage']}%")
        print(f"Status:        {server['status']}")
    else:
        print(f"Server {server['hostname']} is not ready for deployment. CPU, RAM, or Disk usage are high or server is not running.")

    if  server['status'] == "Running":
        ready_server += 1
    elif server['status'] == "stopped":
        stopped_server += 1

print("=" * 30)
print("Deployement Summary")
print("=" * 30)
print(f"Ready server: {ready_server}")
print(f"Stopped server: {stopped_server}")
print(f"Total server: {len(servers)}")
print("=" * 30)

if ready_server == total_servers:
    print("All Servers are ready\nDeployment Approved")
else:
    print("Deployment Blocked")

print(datetime)