# Linux Service Health Checker
# Aurthor: Ali Haider

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
        "memory": 55,
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