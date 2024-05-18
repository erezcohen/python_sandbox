# A variable is a container for a value, which can be of various types

"""
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
"""

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

a = 1
b: int = 2

s1 = "sdfsdf"
s1 = 3
print(type(s1), s1)  # <class 'int'> 3

s2: str = "zazaza"
s2 = 4
print(type(s2), s2)  # <class 'int'> 4


# Multiple assignment (from a tuple?)
x, y, name, is_cool = (1, 2.5, "John", True)
# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # bool

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)  # <class 'float'> 2.0

# div and floor
d = 5 // 2
print(type(d), d)  # <class 'int'> 2
