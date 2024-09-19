import subprocess

result = subprocess.run(["python", "ls-cmd.py"], capture_output=True, text=True)

print(result.stdout)

#if file isn't present


#result = subprocess.run(["python", "file_donot_exist.py"], capture_output=True, text=True, check=False)

#print(result.stdout)

#print(result.stderr)
