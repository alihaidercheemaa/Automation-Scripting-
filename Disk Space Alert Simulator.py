server_name = input("Enter the server name : ").strip().lower()
disk_usage = float(input("Enter the disk usage percentage : ").strip())

if disk_usage >= 0 and disk_usage <= 69:
    print(f"Alert: {server_name} has heaalthy disk usage: {disk_usage}%")
elif disk_usage >= 70 and disk_usage <= 89:
    print(f"Info: {server_name} has normal disk usage: {disk_usage}%")