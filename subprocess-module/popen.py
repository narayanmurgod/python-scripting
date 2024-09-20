import subprocess

p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, errors = p.communicate()

print(output)

#Popen is a class that starts the specified command as a new process. PIPE is used to capture the standard output and standard error of the subprocess.
#The command being run is python --help, which outputs the help information for the Python interpreter.
#stdout=subprocess.PIPE means that the standard output (the output you’d normally see in the terminal) is captured so it can be accessed programmatically.
#stderr=subprocess.PIPE captures any error messages.
#text=True indicates that the output should be treated as text (string) rather than bytes.