## Conditional Statements

## if statement - executes when condition is true otherwise enters the else block

age=20

if age>=18:
    print("Able to Vote")
else:
    print("Can't Vote")


## elif - allows you to check for multiple conditions

age = 20

if age<13:
    print("You are a child")
elif age<18:
    print("You are a teenager")
else:
    print("You are an adult")


## Nested Conditional Statements

num=int(input("Enter the number "))

if num>=0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")



