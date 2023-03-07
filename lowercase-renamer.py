import os

# Get a list of all files in the current directory
files = os.listdir()

# Loop through each file
for file in files:
    # If it's a file (not a directory)
    if os.path.isfile(file):
        # Rename the file to lowercase
        os.rename(file, file.lower())
