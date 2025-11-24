a=100

## declaring and assigning variable

age=21
height=5.8
name="Sujal"
is_student=True

#print patterns

print(f'My name is {name} and my age is {age}')

# some valid variable names

rank="Major"
name="Ghost"

# some invalid variable name
# army-rank

## Variable Types - Python is dynamically typed and data type is determined at the time of runtime

age=18 # int
name="Sujal" #string
is_student=True  # boolean
height=5.8 # float

print(f'Age type {type(age)}, Name Type {type(name)}')

# Type Conversion

age=18
age_str=str(age)
print(age_str)

age_num=int(age_str)
print(age_num)

'''
Error

name="Sujal"
name_int=int(name)
'''


height=5.8

height = float(int(height))

# height will loose its precision

## Dynamic Typing - Python allows a type of variable to change as the prog executes


## input

age=int(input("what is the age "))
print(f'{age} and type is {type(age)}')
