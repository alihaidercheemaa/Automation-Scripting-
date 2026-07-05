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

count_success = 0
count_failed = 0

for i, server in enumerate(servers, start=1):
    print("=" * 30)
    # mark every 3rd server as failed
    if i % 3 == 0:
      status = "Failed"
    else:
      status = "Success"
    print(f"Server Number: {i}")
    print(f"Pinging server: {server}")
    print(f"Status: {status}")

    if status == "Success":
      count_success += 1
    else:
      count_failed += 1



print(f"Successful Pings: {count_success}")
print(f"Failed Pings: {count_failed}")

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))