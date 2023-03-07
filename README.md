# lowercase-renamer
A simple Python program that renames all files in the current directory to lowercase.

This program first imports the os module, which provides a way to interact with the file system.
It then uses the os.listdir() function to get a list of all files in the current directory.
It loops through each file and checks if it's a file (not a directory) using the os.path.isfile() function.
If it is a file, it renames it to lowercase using the os.rename() function and passing in the original file name and the lowercase version of the file name.

-ChatGPT

*Project done with the help of ChatGPT
