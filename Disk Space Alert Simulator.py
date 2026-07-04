
from datetime import datetime


server_name = input("Enter the server name : ").strip().lower()
environment = input("Enter the environment (dev/stage/prod) : ").strip().lower()
disk_usage = float(input("Enter the disk usage percentage : ").strip())


if disk_usage >= 0 and disk_usage <= 69:
    if environment == "prod":
        print(f"status: {server_name} is healthy")
    else:
        print(f"status: {server_name} is healthy")
elif disk_usage >= 70 and disk_usage <= 89:
    if environment == "prod":
        print(f"status: {server_name} has warning high disk usage")
    else:
        print(f"status: {server_name} check it before it went to production")
elif disk_usage >= 90 and disk_usage <= 100:
    if environment == "prod":
        print(f"status: {server_name} is critical")
    else:
        print(f"status: {server_name} check it before it went to production")
else:
    print("Error: Invalid disk usage percentage entered. Please enter a value between 0 and 100.")

print(datetime.now())    