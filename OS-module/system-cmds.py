import os

# Execute the 'ls -l' command
os.system("ls -l")

# Execute the 'date' command and capture the output
output = os.popen("date").read()
print(f"Current date: {output}")
