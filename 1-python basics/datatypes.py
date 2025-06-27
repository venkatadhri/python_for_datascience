# Python Data Types and Their Importance

# Data types define the kind of value a variable can hold.
# They are important because they help Python know how to store, process, and operate on data.

# Basic Data Types in Python:

# 1. Integer (int)
# - Whole numbers, positive or negative, without decimals.
# - Used for counting, indexing, and arithmetic operations.

x = 10
print("Integer:", x)
print("Type of x:", type(x))

# 2. Float
# - Numbers with decimal points.
# - Used for measurements, scientific calculations, and precise values.

y = 3.14
print("Float:", y)
print("Type of y:", type(y))

# 3. String (str)
# - Sequence of characters, used to store text.
# - Useful for names, messages, and any textual data.

name = "Python"
print("String:", name)
print("Type of name:", type(name))

# 4. Boolean (bool)
# - Represents True or False values.
# - Used for conditional logic and comparisons.

is_active = True
print("Boolean:", is_active)
print("Type of is_active:", type(is_active))



# Core Data Types in Python:

# 1. List
# - Ordered, mutable (changeable) collection of items.
# - Can store items of different types.
# - Useful for storing sequences of items.

# Example:
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
fruits.append("orange")  # Add item
print("After append:", fruits)
print("First fruit:", fruits[0])  # Access by index

# 2. Tuple
# - Ordered, immutable (unchangeable) collection of items.
# - Useful for fixed data that should not change.

# Example:
coordinates = (10, 20)
print("Tuple:", coordinates)
print("X coordinate:", coordinates[0])

# 3. Dictionary (dict)
# - Unordered collection of key-value pairs.
# - Keys must be unique and immutable.
# - Useful for mapping and fast lookups.

# Example:
person = {"name": "Alice", "age": 25}
print("Dictionary:", person)
print("Name:", person["name"])
person["age"] = 26  # Update value
print("Updated age:", person["age"])

# 4. Set
# - Unordered collection of unique items.
# - Useful for removing duplicates and set operations (union, intersection).

# Example:
numbers = {1, 2, 3, 2, 1}
print("Set (duplicates removed):", numbers)
numbers.add(4)
print("After adding 4:", numbers)

# Summary:
# - Lists: Use when you need an ordered, changeable collection.
# - Tuples: Use for ordered, unchangeable data.
# - Dictionaries: Use for key-value mapping.
# - Sets: Use for unique items and set operations.