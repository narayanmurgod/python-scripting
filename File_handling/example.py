#Working with Directories
import os
import os.path
import shutil

#os.mkdir('folder1')
dir_list = os.listdir('.') # Dot represents the current directory 
print(dir_list)

is_there=os.path.exists('myfile.txt') # exist funtion checks if the provided file present or not
print(f"The file is present?",is_there)

file_inside_folder1=open('experince.txt', 'w')
file_inside_folder1.write("I have a two years of experience on GCP")

os.remove('myfile.txt') # Delete a file

os.rmdir('mydir') # Delete an empty directory

shutil.rmtree('mydir') # Recursively delete a directory

file.close() #Remember to always handle files carefully, and make sure to close them after you're done to free up system resources.