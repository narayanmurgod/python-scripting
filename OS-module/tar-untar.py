import os
import tarfile

def tar_files(source_dir, destination_file):
    """
    Tars a directory of files into a single tar file.

    Args:
        source_dir: The directory containing the files to tar.
        destination_file: The name of the tar file to create.
    """

    with tarfile.open(destination_file, "w:gz") as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                tar.add(os.path.join(root, file))

def untar_file(source_file, destination_dir):
    """
    Untars a tar file into a directory.

    Args:
        source_file: The name of the tar file to untar.
        destination_dir: The directory to extract the files into.
    """

    with tarfile.open(source_file, "r:gz") as tar:
        tar.extractall(path=destination_dir)

# Example usage:
source_dir = "."
destination_file = "archive.tar.gz"
destination_dir = "untared_files"

#tar_files(source_dir, destination_file)
untar_file(destination_file, destination_dir)