import os

#os.path.exists(path): Checks if a path exists (returns True if it does, False otherwise).
file = 'example.txt'
if os.path.exists(file):
    print(f"{file} exists")
else:
    print(f"{file} does not exist")

#os.path.isfile(path): Checks if a path is a file (returns True if it is, False otherwise).
if os.path.isfile(file):
    print(f"{file} is a file")

size = os.path.getsize(file)
print(f"Size of {file}: {size} bytes")

os.rename('example.txt', 'renamed_example.txt')

