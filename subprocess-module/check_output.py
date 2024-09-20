import subprocess

try:

    output = subprocess.check_output(["python", "--ve0rsion"], text=True)

    print(output)

except subprocess.CalledProcessError as e:

    print(f"Command failed with return code {e.returncode}")

#check_output is a function in the subprocess module that is similar to run(), but it only returns the standard output of the command, and raises a CalledProcessError exception if the return code is non-zero.
#o/p
#unknown option --ve0rsion
#usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
#Try `python -h' for more information.
#Command failed with return code 2