# Resuable Backup  Functions
# Aurthor: Ali Haider

print("=" * 40)
print("       DevOps Backup Automation")
print("=" * 40)

servers = ["web_prod_1",
          "web_prod_2",
          "api_prod_1",
          "payment_prod_1",
          "login_prod_1",
          "db_prod_1",
          "cache_prod_1",
          "logs_prod_1",
          "backup_prod_1",
          "db_backup_prod_1"
          ]

def backup_server(server_name):
        print("backup starting .....")
        print(f"Backing up: {server_name}")
        print("Backup completed")


def backup_status(server_name):
        return "Success"

Sucessful_backup = 0
Failed_backup = 0
total_servers = len(servers)

for server in servers:
    backup_server(server)
    status = backup_status(server)
    print(f"Status for {server}: {status}")
    
    if  status == "Success":
        Sucessful_backup += 1
    elif status == "Failed":
        Failed_backup += 1

print("=" * 30)
print("Backup Summary")
print("=" * 30)
print(f"Ready server: {Sucessful_backup}")
print(f"Stopped server: {Failed_backup}")
print(f"Total server: {len(servers)}")
print("=" * 30)
