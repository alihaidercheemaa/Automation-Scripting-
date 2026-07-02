# Automation script to generate server names

server_type = input("Enter the server type : ").strip().lower()
environment = input("Enter the environment : ").strip().lower()
server_number = input("Enter the server number : ").strip()


print(f"Generated Server Name: {server_type}-{environment}-{server_number}")
