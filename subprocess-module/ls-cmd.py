import subprocess

# Execute a command and capture its output
output = subprocess.check_output(["ls", "-l"], text=True)
print(output)  # Decode bytes to string

