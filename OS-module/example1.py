import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Create a new directory
new_directory = "my_new_directory"
os.makedirs(new_directory, exist_ok=True)
print(f"Created directory: {new_directory}")

# List files in the current directory
files = os.listdir()
print("Files in the current directory:", files)

# Get the size of a file
file_path = "my_file.txt"
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    print(f"Size of {file_path}: {file_size} bytes")
else:
    print(f"File {file_path} does not exist.")

# Rename a file
old_name = "my_file.txt"
new_name = "renamed_file.txt"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}")
else:
    print(f"File {old_name} does not exist.")

# Delete a file
file_to_delete = "renamed_file.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"Deleted {file_to_delete}")
else:
    print(f"File {file_to_delete} does not exist.")
