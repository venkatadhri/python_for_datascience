## single  line comment
# print("hello world")  # this is a comment

"""
This is a multi-line comment
It can span multiple lines
"""
print("hello world")  # this is a comment

# Variables and data types
x = 5  # integer
y = 3.14  # float
name = "Alice"  # string
is_active = True  # boolean

# Printing variables
print(x)  # prints: 5
print(y)  # prints: 3.14
print(name)  # prints: Alice
print(is_active)  # prints: True    

# Basic arithmetic operations
a = 10
b = 3

sum_result = a + b  # addition
diff_result = a - b  # subtraction
prod_result = a * b  # multiplication
div_result = a / b  # division
mod_result = a % b  # modulus
exp_result = a ** b  # exponentiation

print("Sum:", sum_result)  # prints: Sum: 13
print("Difference:", diff_result)  # prints: Difference: 7
print("Product:", prod_result)  # prints: Product: 30
print("Division:", div_result)  # prints: Division: 3.3333333333333335
print("Modulus:", mod_result)  # prints: Modulus: 1
print("Exponentiation:", exp_result)  # prints: Exponentiation: 1000

# String operations
greeting = "Hello"
name = "Bob"
full_greeting = greeting + ", " + name + "!"  # string concatenation
print(full_greeting)  # prints: Hello, Bob!

# String formatting
age = 30
formatted_string = f"{name} is {age} years old."  # f-string formatting
print(formatted_string)  # prints: Bob is 30 years old.     

# List operations
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # adding an item to the list
print(fruits)  # prints: ['apple', 'banana', 'cherry', 'orange']

# Accessing list items
first_fruit = fruits[0]  # accessing the first item
print(first_fruit)  # prints: apple

## understing semantics
# Looping through a list
for fruit in fruits:
    print(fruit)  # prints each fruit in the list
    # Conditional statements
    if fruit == "banana":
        print("Found a banana!")
    else:
        print("Not a banana.")

## type Interference
# Python automatically infers the type of a variable based on the value assigned to it.
# For example, if you assign an integer to a variable, Python treats it as an integer.
# If you later assign a string to the same variable, Python will treat it as a string.
# This dynamic typing allows for flexibility but requires careful handling to avoid type-related errors.
# Example:
x = 10  # x is an integer
print(type(x))  # prints: <class 'int'>

x = "Hello"  # now x is a string
print(type(x))  # prints: <class 'str'>

# Python's dynamic typing means you don't need to declare variable types explicitly.# However, it can lead to runtime errors if you try to perform operations on incompatible types.
# For example:
try:
    result = x + 5  # This will raise an error because x is a string
except TypeError as e:
    print(f"Error: {e}")  # prints: Error: can only concatenate str (not "int") to str
    
# To avoid such errors, you can use type checking or type conversion functions like `int()`, `float()`, or `str()` to ensure the correct type is used.
# Example of type conversion:
x = "10"  # x is a string
x_int = int(x)  # convert string to integer
print(type(x_int))  # prints: <class 'int'>

# Python's dynamic typing allows for flexibility, but it requires careful handling to avoid type-related errors.
# Example of type checking:
if isinstance(x, str):
    print("x is a string")  # prints: x is a string
else:
    print("x is not a string")


#indentation
# Python uses indentation to define blocks of code. Indentation is crucial for defining the structure of loops, functions, and classes.
# For example:
def greet(name):
    print(f"Hello, {name}!")  # This line is indented, indicating it belongs to the greet function

greet("Alice")  # prints: Hello, Alice!

# If you don't use consistent indentation, Python will raise an IndentationError.
try:
    def faulty_function():
        print("This line is indented")
    print("This line is not indented")  # This will raise an IndentationError
except IndentationError as e:
    print(f"Indentation Error: {e}")  # prints: Indentation Error: expected an indented block
    
# Python's indentation rules are strict, and mixing tabs and spaces can lead to errors.
# It's recommended to use either spaces or tabs consistently throughout your code.
# The Python community generally prefers using 4 spaces for indentation.
# Example of consistent indentation:
def consistent_function():
    print("This line is indented with 4 spaces")

consistent_function()  # prints: This line is indented with 4 spaces

