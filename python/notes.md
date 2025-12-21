### Global Variable ###
x = 10

def update():
    global x 
    x=20

update()
print(x)

### Some Generic Terms ###

- Module = Python File
- Folder with __init__.py = Package
- Folder inside Folder = Subpackage


### Use of __name__ == "main" ###

- while importing a module prevents its execution