import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List all files and directories in the current directory
files_and_dirs = os.listdir()
print("Files and directories in current directory:")
for item in files_and_dirs:
    print(item)

# Create a new directory
new_dir = 'new_directory'
#os.mkdir(new_dir)
#print(f"Directory '{new_dir}' created")

# Change to the new directory
os.chdir(new_dir)
print(f"Changed working directory to: {os.getcwd()}")

# Create a new file in the new directory
file_name = 'example.txt'
with open(file_name, 'w') as file:
    file.write("Hello, world!.........today")
print(f"File '{file_name}' created")

# Change back to the original directory
os.chdir('..')
print(f"Changed working directory back to: {os.getcwd()}")

# Remove the file and the directory
os.remove(os.path.join(new_dir, file_name))
os.rmdir(new_dir)
print(f"File '{file_name}' and directory '{new_dir}' removed")