import os  # python

# Current file name
file1 = "input.txt"

# New file name
file2 = "output.txt"

# Rename the file
os.rename(file1,file2)
print(file1,file2)  # unformatted
#formatted output
print(f"File '{file1}' renamed to '{file2}' successfully.")