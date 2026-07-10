# Linux User Management using list, Dictionary, loops and conditional logic
# Aurthor: Ali Haider

print("=" * 30)
print("     Linux User Management")
print("=" * 30)

server_users = [
    {
    "username": "Ali",
    "role": "DevOps",
    "status": "active",
    "sudo": True
    },
    {
    "username": "Nabeel",
    "role": "AI Engineer",
    "status": "active",
    "sudo": True
    },
    {
    "username": "Talha",
    "role": "Azure DevOps",
    "status": "active",
    "sudo": True
    },
    {
    "username": "Zaid",
    "role": "AI Developer",
    "status": "active",
    "sudo": True
    },
    {
    "username": "Abdullah",
    "role": "QA",
    "status": "inactive",
    "sudo": False
    },
    {
    "username": "Bilal",
    "role": "Game Developer",
    "status": "inactive",
    "sudo": False
    },
    {
    "username": "Husnain",
    "role": "Data Analysis Expert",
    "status": "active",
    "sudo": False
    },
    {
    "username": "Mamoon",
    "role": "Security Expert",
    "status": "active",
    "sudo": True
    },
    {
    "username": "Hassan",
    "role": "Frontend Developer",
    "status": "active",
    "sudo": False
    },
    {
    "username": "Usman",
    "role": "Backend Developer",
    "status": "active",
    "sudo": True
    }
    ]

def check_user(user):
    # Expecting a dict with keys: username, role, status, sudo
    print(f"Username: {user['username']}")
    print(f"Role: {user['role']}")
    print(f"status: {user['status']}")
    print(f"sudo: {user['sudo']}")

def deployment_access(user):
    # user is expected to be a dict; allow deployment only if status is 'active' and sudo is True
    if user['status'] == 'active' and user['sudo']:
        return "Allowed"
    else:
        return "denied"

deployment_allowed = 0
deployment_denied = 0
active_users = 0
inactive_users = 0
total_users = len(server_users)

for user in server_users:
    print("=" * 30)
    check_user(user)
    status = deployment_access(user)
    print(f"Status: {status}")

    if status == "Allowed":
        deployment_allowed += 1
    elif status == "denied":
        deployment_denied += 1
    
    if user["status"] == "active":
        active_users += 1
    elif user["status"] == "inactive":
        inactive_users += 1


print("=" * 30)
print("LINUX USER MANAGEMENT SYSTEM")
print("=" * 30)
print(f"Total Users: {total_users}")
print(f"Active Users: {active_users}")
print(f"Inactive Users: {inactive_users}")
print(f"Deployment Allowed: {deployment_allowed}")
print(f"Deployment Denied: {deployment_denied}")
print("=" * 30)