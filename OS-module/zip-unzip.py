import zipfile
import os

def zip_files(source_dir, destination_file):
    with zipfile.ZipFile(destination_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to zip archive with relative path
                zipf.write(file_path, arcname=os.path.relpath(file_path, start=source_dir))

def unzip_file(source_file, destination_dir):
    with zipfile.ZipFile(source_file, 'r') as zipf:
        zipf.extractall(path=destination_dir)

# Example usage:
source_dir = "."  # Current directory
destination_file = "archive.zip"
destination_dir = "unzipped_files"

# Create a zip archive of the current directory
zip_files(source_dir, destination_file)

# Extract the contents of the zip archive to a specified directory
unzip_file(destination_file, destination_dir)
