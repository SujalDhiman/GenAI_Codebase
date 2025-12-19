## try, except block

try:
    a=b
except:
    print("Variable has not been assigned")


## All types of error like TypeError, ZeroDivisionError are derived from main exception class

## Exception class can handle any type of exception


try:
    result=1/0
    a=b
except Exception as ex:
    print(ex)


## try, except, else block

## else block is a continuation of try block

try:
    num=int(input("Enter a number: "))
    result=10/num
except Exception as ex:
    print(ex)
else:
    print(f'Continuation to try block')


## try, except, else and finally

# finally - it gets executed whether error arises or not

try:
    num=int(input("Enter a number: "))
    result=10/num
except Exception as ex:
    print(ex)
else:
    print(f'Continuation to try block')
finally:
    print(f'Execution Completed')



