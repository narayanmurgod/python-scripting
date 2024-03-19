#Opening and Closing Files

# Opening a file in read mode
file = open('myfile.txt', 'r')

# Opening a file in write mode
file = open('myfile.txt', 'w')

# Opening a file in append mode
file = open('myfile.txt', 'a')

# Always close the file after you're done with it
file.close()


# Reading the entire file
content = file.read()

# Reading one line at a time
line = file.readline()

# Reading all lines into a list
lines = file.readlines()

#Writing to File. This method overwrites the content of the file
file.write("Hello, World!\n")

#Writing to Files. This appends the previously written content
file = open('myfile.txt', 'a')
file.write("New content\n")

