## Dictionaries - are unordered collection of items. The data is stored in key value pair. Key should be unique and immutable

## Creating Dictionaries

empty_dict={}

empty_dict=dict()

obj = {"name":"Sujal","age":21,"is_student":True}

print(obj)

print(obj["is_student"])

# Access using get method

print(obj.get('name'))

print(obj.get('last_name')) # u will get none if key is not present

print(obj.get('last_name',"Not Available")) # giving a value if key is not present


# Dictionary are mutable, so you can add, update or delete elements

obj["age"]=33 # update

obj["address"]="ddn" # added

del obj['age']
print(obj)

## Dictionary Methods

keys= obj.keys()

vals= obj.values()

items = obj.items()

print(keys,vals,items)

## shallow copy (updates in original will not be reflected in copied)

obj_copy = obj

obj["name"]="Ghost"
print(obj)
print(obj_copy)

## creating shallow copy

obj_copy=obj.copy()

obj["name"]="Sujal"
print(obj)
print(obj_copy)

## Iterating

for keys in obj.keys():
    print(keys)


for vals in obj.values():
    print(vals)


for key,value in obj.items():
    print(key,value)


## Nested Dictionaries

students = {
    "student1":{
        "name":"A",
        "age":20,
    },
    "student2":{
        "name":"B",
        "age":"18"
    }
}


## Dictionary Comprehension

sqauares = {"x":x**2 for x in range(5)}
print(sqauares)

evens = {x:x**2 for x in range(5) if x%2 == 0}
print(evens)


## to check if key is present

print("name" in obj)

# merging dictionaries

d1={"a":1,"b":2}
d2={"c":3,"d":4}

print({**d1,**d2})
