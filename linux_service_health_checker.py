# Linux Service Health Checker
# Author: Ali Haider

services = [
    {
        "service": "nginx",
        "status": "running",
        "cpu": 18,
        "memory": 42,
        "restart_count": 0
    },
    {
        "service": "docker",
        "status": "running",
        "cpu": 35,
        "memory": 56,
        "restart_count": 1
    },
    {
        "service": "postgresql",
        "status": "running",
        "cpu": 48,
        "memory": 68,
        "restart_count": 0
    },
    {
        "service": "redis",
        "status": "running",
        "cpu": 22,
        "memory": 30,
        "restart_count": 2
    },
    {
        "service": "prometheus",
        "status": "running",
        "cpu": 40,
        "memory": 72,
        "restart_count": 1
    },
    {
        "service": "grafana",
        "status": "running",
        "cpu": 28,
        "memory": 50,
        "restart_count": 0
    },
    {
        "service": "jenkins",
        "status": "running",
        "cpu": 82,
        "memory": 76,
        "restart_count": 4
    },
    {
        "service": "rabbitmq",
        "status": "stopped",
        "cpu": 0,
        "memory": 0,
        "restart_count": 6
    },
    {
        "service": "node_exporter",
        "status": "running",
        "cpu": 12,
        "memory": 18,
        "restart_count": 0
    },
    {
        "service": "vault",
        "status": "running",
        "cpu": 25,
        "memory": 45,
        "restart_count": 0
    }
]

def display_services(service):
    print(f"Service: {service['service']}")
    print(f"CPU: {service['cpu']}%")
    print(f"Memory: {service['memory']}%")
    print(f"Restart Count: {service['restart_count']}")

def check_service(service):
    if (
        service["status"] == "running"
        and service["cpu"] < 80
        and service["memory"] < 80
        and service["restart_count"] < 5
    ):
        return "Healthy"
    else:
        return "Unhealthy"
    
healthy_services = 0
unhealthy_services = 0
running_services = 0
stopped_services = 0
total_services = len(services)

for service in services:
    print("=" * 30)
    display_services(service)
    status = check_service(service)
    print(f"Status: {status}")

    if service['status'] == 'running':
        running_services += 1
    else:
        stopped_services +=1

    if status == "Healthy":
        healthy_services +=1
    else:
        unhealthy_services +=1

print("=" * 30)
print("INFRASTRUCTURE SUMMARY")
print("=" * 30)
print(f"Total Services: {total_services}")
print(f"Running Services: {running_services}")
print(f"Stopped Services: {stopped_services}")
print(f"Healthy Services: {healthy_services}")
print(f"Unhealthy Services: {unhealthy_services}")


if healthy_services == total_services:
    print("\nDeployment Status : Allowed")
else:
    print("\nDeployment Status : Denied")


print("=" * 30)