# Linux User Management using list, Dictionary, loops and conditional logic
# Aurthor: Ali Haider

print("=" * 40)
print("       Linux User Management")
print("=" * 40)

server_users = [
    {
    "username": "Ali",
    "role": "devops",
    "status": "active",
    "sudo": True
    },
    {
    "username": "nabeel",
    "role": "ai engineer",
    "status": "active",
    "sudo": True
    },
    {
    "username": "talha",
    "role": "azure devops",
    "status": "active",
    "sudo": True
    },
    {
    "username": "zaid",
    "role": "ai developer",
    "status": "active",
    "sudo": True
    },
    {
    "username": "abdullah",
    "role": "qa",
    "status": "unactive",
    "sudo": False
    },
    {
    "username": "bilal",
    "role": "game developer",
    "status": "unactive",
    "sudo": False
    },
    {
    "username": "husnain",
    "role": "data analysis expert",
    "status": "active",
    "sudo": False
    },
    {
    "username": "mamoon",
    "role": "security expert",
    "status": "active",
    "sudo": True
    },
    {
    "username": "hassan",
    "role": "frontend developer",
    "status": "active",
    "sudo": False
    },
    {
    "username": "usman",
    "role": "backend developer",
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

for users in server_users:
    check_user(users)
    status = deployment_access(users)
    print(f"Status: {status}")