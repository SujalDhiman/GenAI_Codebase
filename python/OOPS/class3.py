## Attriubte Shadowing in Python

class Chai:
    temperature="hot"
    strength="Strong"

cutting = Chai()

print(cutting.temperature)

cutting.temperature="Mild"

print(cutting.temperature)
print(Chai.temperature)

del cutting.temperature
print(cutting.temperature) # here fall back occurs and value is referred from main class

cutting.size="small" # we injected this

del cutting.size
print(cutting.size) # error occur since class does not have this attribute