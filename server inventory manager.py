#input all the details of the server from the user

owner = input("Enter the owner : ").strip().lower()
hostname = input("Enter the hostname : ").strip().lower()
ip_address = input("Enter the IP address : ").strip()
operating_system = input("Enter the operating system : ").strip().lower()
environment = input("Enter the environment (dev/stage/prod) : ").strip().lower()
cpu_cores = int(input("Enter the number of CPU cores : ").strip())
ram_size = int(input("Enter the RAM size (in GB) : ").strip())
status = input("Enter the status (active/inactive) : ").strip().lower()

# Store the server details in a dictionary

server_details = {

    "Owner": owner,
    "Hostname": hostname,
    "IP Address": ip_address,
    "Operating System": operating_system,
    "Environment": environment,
    "CPU Cores": cpu_cores,
    "RAM Size": ram_size,
    "Status": status
}

# Display the server details in a formatted manner

print("=" * 40)
print("\nServer Inventory Details:")
print("=" * 40)

print(f"Owner:            {server_details['Owner']}")
print(f"Hostname:         {server_details['Hostname']}")
print(f"IP Address:       {server_details['IP Address']}")
print(f"Operating System: {server_details['Operating System']}")
print(f"Environment:      {server_details['Environment']}")
print(f"CPU Cores:        {server_details['CPU Cores']}")
print(f"RAM Size:         {server_details['RAM Size']} GB")
print(f"Status:           {server_details['Status']}")

print("=" * 40)

# Display the total number of values in the inventory

print(f"Total values in inventory: {len(server_details)}") 