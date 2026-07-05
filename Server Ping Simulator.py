# Project: Disk Space Alert Simulator
# Author: Ali Haider
# Description:
# Ping multiple servers in a list using loops

from datetime import datetime

servers = [
    "web-prod-01",
    "web-prod-02",
    "db-prod-01",
    "api-prod-01",
    "cache-prod-01",
    "backup-prod-01",
    "proxy-prod-01",
    "worker-prod-01",
    "monitor-prod-01",
    "storage-prod-01"
]

for i, server in enumerate(servers, start=1):
    print("=" * 30)
    # mark every 3rd server as failed
    if i % 3 == 0:
     status = "Failed"
    else:
     status = "Success"
    print(f"Pinging server: {i}. {server}")
    print(f"Status: {status}")

count_success = sum(1 for i in range(1, len(servers) + 1) if i % 3 != 0)
count_failed = len(servers) - count_success

print(f"Successful Pings: {count_success}")
print(f"Failed Pings: {count_failed}")

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))