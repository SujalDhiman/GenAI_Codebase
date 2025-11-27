## Tuples - are ordered collection of items that are immutable. They are similar to lists, but their immutability makes them different


# creating a tuple

empty_tuple = ()

print(empty_tuple,type(empty_tuple))

lst = list()
tup = tuple()

numbers = tuple([1,2,3,4,5,6]) # and vice versa

mixed_tuple = (1,"a","b",True,3.14)

## Accessing Tuple Elements

print(mixed_tuple[4])

## same slicing/index as worked in list

## Tuple Operations

num = mixed_tuple[::1]

new_tuple = num + mixed_tuple

print(new_tuple)

new_tuple = new_tuple * 2 # the initial list is repeated

print(new_tuple)

## Immutable Nature of Tuple

lst = [1,2,3,4,5]

lst[1]="a"

print(lst)

tup = (1,2,3,4,5)

# error not allowed tup[2]=3

print(tup.count(1))

print(tup.index(3)) # where this element is located


## Packing and Unpacking a TUple

new_tup="a",3.14,1,2

print(new_tup) # packing

a,b,c,d=new_tup

print(a,b,c,d) # unpacking

numbers=(1,2,3,4,5,6)

first,*middle,end=numbers

print(first,type(middle),end) # imp

# Nested Tuple





