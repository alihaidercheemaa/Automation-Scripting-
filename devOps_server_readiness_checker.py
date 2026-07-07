# Script for checking whether the server is ready for deployment or not.
# Author : Ali Haider

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
    "cpu_usage": 53,
    "ram_usage": 67,
    "disk_usage": 71,
    "status": "Running"
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
    "cpu_usage": 32,
    "ram_usage": 45,
    "disk_usage": 50,
    "status": "Running"
    }
]

for server in enumerate(servers):
    if servers: