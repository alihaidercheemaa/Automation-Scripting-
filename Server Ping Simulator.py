# Project: Disk Space Alert Simulator
# Author: Ali Haider
# Description:
# Ping multiple servers in a list using loops

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
    print(f"Pinging server: {i}. {server}")
    print(f"Status: Successfully")


print("=" * 30)
print("Total Servers Checked:", len(servers))
print("\nSimulation Completed.")
print("=" * 30)