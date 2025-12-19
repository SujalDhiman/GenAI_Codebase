## create a new directory
import os

new_directory="package"

# os.mkdir(new_directory)

print(f'Directory {new_directory} created')


## Listing files and directory

items=os.listdir('.')
print(items)

## Joining Paths

dir_name="folder"
file_name="file.txt"

full_path=os.path.join(dir_name,file_name)

print(full_path)

full_path=os.path.join(os.getcwd(),dir_name,file_name)

print(full_path)


# Checking if a path is file or directory

path='example.txt'

if os.path.isdir(path):
    print("directory")
elif os.path.isfile(path):
    print("File")
else:
    print("Does not exist")



