# Lists - are ordered and mutable collection of items and contains data of different types


lst=[]

print(type(lst))

names=["a","b","c",1,2,3]

print(names)


# Accessing List Items

print(names[2])
print(names[-4]) # last element is at idx -1

print(names[1:])

print(names[1:3]) # elements from start to end-1

# modify the list elements

names[1]="Sujal"

print(names)

# List Methods

names.append(3.14) # add an item to the end

names.insert(1,"Car") # to add at an index

names.remove("Sujal") # to remove element

## remove and return the last word

item = names.pop()

## to get the index of element

print(names.index('a'))

## to count an element

print(names.count('a'))

num=[10,1,2,6,7,45]

## to sort the list
num.sort()

print(num)

num.clear() # removes all items from list


## Slicing Lists

print("#####################################")

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

print("Iterating over list")

for i in numbers:
    print(i)


print("Iterating with index")

for index,number in enumerate(numbers):
    print(index," ",number)


print("List comprehension")

lst= []

for i in range(10):
    lst.append(i*i)

# now list comprehension

lst1 = [x**2 for x in range(10)]
print(lst1)

## Syntax for List Comprehension

# Basics Syntax [expression for item in iterable]

# with logic [expression for item in iterable if condition]

arr = [i for i in range(10) if i%2 == 0]
print(arr)

## Nested List Comprehension

# [expression for item1 in i1 for item2 in i2]

