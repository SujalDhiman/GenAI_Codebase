# DataTypes - classification of data which tell the compiler how the programmer intends to use the data

## Integers

age=35
type(age)

## Float

width=10.45
print(f'width is of type {type(width)}')

## String

name="Sujal"
print(type(name))

## boolean data types

is_true=True
print(type(is_true))

a=10
b=20

print(type(a==b))

## common errors

result="Hello" + 5  # error: can only concatenate string not int
print(result)

# fix for above is 
result="Helllo" + str(5)


