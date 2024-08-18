import os

# Get the value of the HOME environment variable
home_dir = os.environ.get("HOME")
print(f"HOME directory: {home_dir}")

# Get the value of the PATH environment variable
path_var = os.environ.get("PATH")
print(f"PATH variable: {path_var}")
