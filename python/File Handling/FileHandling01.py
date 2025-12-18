## File Operations

with open('example.txt','r') as file:
    content=file.read()
    print(content)


## reading line by line

with open('example.txt','r') as file:
    for line in file:
        print(line.strip())


## writing in a file

with open('example.txt','w') as file:
    file.write('Hello Python')


## appending in a file

with open('example.txt','a') as file:
    file.write("GenAI Course Learning")


with open('example.txt','r') as file:
    content=file.read()


with open('destination.txt','w') as destination_file:
    destination_file.write(content)



# The w+ mode in python is used to open a file for both reading and writing. If the file does not exist, it will be created. If the file exists, its content is truncated.

with open('test1.txt','w+') as file:
    file.write("Hello World\n")
    file.write("this is a new line \n")

    ## moving the cursor to the beginning to read file

    file.seek(0)
    content=file.read()

    print(content)

