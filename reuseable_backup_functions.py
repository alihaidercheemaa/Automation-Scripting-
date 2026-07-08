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
        return "succes"


server = backup_server("web_prod_1")
print(server)