import os

# Get the operating system name
os_name = os.name
print(f"Operating system name: {os_name}")

# Get the current user
current_user = os.getlogin()
print(f"Current user: {current_user}")

# Get the processor architecture
arch = os.uname().machine
print(f"Processor architecture: {arch}")
