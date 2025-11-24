## Loops

print(range(5))  # starts from 0 to end num-1

for i in range(2,5):
    print(i)


# range(start,stop,step) 

for i in range(1,10,3):
    print(i)


for i in range(10,1,-1):
    print(i)


str="Ghost"

for i in str:
    print(i)


## while loop - continues to execute as long as condition is true

count=0

while count<=5:
    print("hi")
    count+=1

print(count)


## Loop Control Statements

## break - exists the loop prematurely

for i in range(10):
    if i == 5:
        break
    print(i)


# continue - skips the current iteration and continues with the next

for i in range(10):
    if i%2==0:
        continue
    print(i)


# pass - it does nothing

for i in range(5):
    if i == 3:
        pass
    print(i)