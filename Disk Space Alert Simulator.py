
server_name = input("Enter the server name : ").strip().lower()
disk_usage = float(input("Enter the disk usage percentage : ").strip())

if disk_usage >= 0 and disk_usage <= 69:
    print(f"Alert: {server_name} has healthy disk usage: {disk_usage}%")
elif disk_usage >= 70 and disk_usage <= 89:
    print(f"Info: {server_name} has high disk usage: {disk_usage}%")
elif disk_usage >= 90 and disk_usage <= 100:
    print(f"Warning: {server_name} has critical disk usage: {disk_usage}%")
else:
    print("Error: Invalid disk usage percentage entered. Please enter a value between 0 and 100.")
    