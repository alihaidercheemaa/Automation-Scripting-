# infrastructure_health_monitor
# Author: Ali Haider   
# Date: 2024-06-15

''' Scenario
    Imagine you're a Junior DevOps Engineer.
    Your team has 10 Linux servers.
    Your task is to write a Python automation script that checks each server and generates a health report.'''

import platform
import os
from datetime import date, datetime, time

print("=" * 50)
print("      DevOps Infrastructure Health Monitor")
print("=" * 50)

print(f"Current Date     : {date.today()}")
print(f"Current Time     : {datetime.now().strftime('%H:%M:%S')}")
print(f"Python Version   : {platform.python_version()}")
print(f"Operating System : {platform.system()} {platform.release()}")