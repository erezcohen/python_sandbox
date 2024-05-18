# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]
mix = ["Apples", 4]

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get the first value
print(fruits[0])

# Get the last value
print(fruits[-1])


# Get length
print(len(fruits))

# Append to list
fruits.append("Mangos")

# Remove the specified item from list
fruits.remove("Grapes")

# Insert into position
fruits.insert(2, "Strawberries")

# Change value
fruits[0] = "Blueberries"

# Remove item from the end
fruits.pop()

# Remove item with the given index
# fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

# Slice (immutable)
print(fruits[0:2])

# Slice to end (immutable)
print(fruits[2:])


# Global funcs

sorted(fruits)
sum(numbers)
max(numbers)

# Contains
print("bananas in fruits:", "bananas" in fruits)

# Can be used to destruct multiple values returned from a func
a, b = [12, 34]
# also:
a, b = 12, 34

print("a, b: ", a, b)
