# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Paul", "Sara", "Susan"]

# Simple for loop (can be over tuples too)
for person in people:
    print(f"Current Person: {person}")

# loop a string
for char in "people":
    print(f"Current char: {char}")

# Break
for person in people:
    if person == "Sara":
        break
    print(f"Current Person: {person}")

# Continue
for person in people:
    if person == "Sara":
        continue
    print(f"Current Person: {person}")

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f"Number: {i}")

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
    print(f"Count: {count}")
    count += 1

#########################################################
# List / Dict Comprehensions
# Similar to map(): iterate over an array
# Alternative to for loops
# Alternative to lambda functions

# List Comprehensions
squars_from_range = [n**2 for n in range(10)]
print("squars from range:", squars_from_range)

# add filtering with "if":
long_names = [name for name in people if len(name) > 4]
print("long names: ", long_names)

# can break into lines:
# long_names = [name for name
#              in people
#              if len(name) > 4]

sum_long_names = sum([len(name) > 4 for name in people])  # [False, False, False, True]

print("Sum long names: ", sum_long_names)

nums = [3, 5, 7]

# array.some(): any
print("list has num divisible by 7:", any([num % 7 == 0 for num in nums]))

# array.every(): all
print("All nums in list are divisible by 7:", all([num % 7 == 0 for num in nums]))


#########################################################

# Dicts Comprehensions
squars_from_range = {str(n): n**2 for n in range(10)}
print("squars dict from range:", squars_from_range)

# this works too (keys can be float, int, string, bool - anything immutable)
# squars_from_range = {n: n**2 for n in range(10)}
