# System information display 
# Importing all the required modules to get the information

import os
import platform
import sys
import getpass
from datetime import datetime

print("      System Information")

print(f"Hostname             : {platform.node()}")

print(f"Operating System     : {platform.system()}")

print(f"OS Version           : {platform.version()}")

print(f"Machine Architecture : {platform.machine()}")

print(f"Processor            : {platform.processor()}")

print(f"Python Version       : {sys.version.split()[0]}")

print(f"Current User         : {getpass.getuser()}")

print(f"Working Directory    : {os.getcwd()}")

print(f"Current date & Tim   :{datetime.now()}")