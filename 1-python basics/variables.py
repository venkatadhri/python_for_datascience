# Python Variables - Complete Guide for Beginners

# 1. What is a Variable?
# A variable is a name that refers to a value stored in memory.

# 2. Creating Variables
x = 10          # integer variable
name = "Alice"  # string variable
pi = 3.14       # float variable

# 3. Variable Naming Rules
# - Can contain letters, numbers, and underscores
# - Cannot start with a number
# - Case-sensitive (age and Age are different)

my_var = 5
MyVar = 6

# Examples of invalid variable names (these will cause errors if uncommented)
# 2nd_name = "John"     # Invalid: starts with a number
# my-var = 10           # Invalid: contains a hyphen
# class = "test"        # Invalid: 'class' is a reserved word
# user name = "Alice"   # Invalid: contains a space

# 4. Assigning Values
a = 100
b = a           # b gets the value of a (100)
a = 200         # changing a does not affect b

# 5. Multiple Assignment
x, y, z = 1, 2, 3
a = b = c = 0   # all three variables get 0

# 6. Data Types
num = 7                 # int
price = 19.99           # float
is_valid = True         # bool
message = "Hello"       # str
items = [1, 2, 3]       # list
person = {"name": "Bob"}# dict

# 7. Type Checking
print(type(num))        # <class 'int'>
print(type(message))    # <class 'str'>

# 8. Changing Variable Type (Type Casting)
x = 5
y = str(x)              # y is now "5" (string)
z = float(x)            # z is now 5.0 (float)

# 9. Deleting Variables
temp = 123
del temp
# print(temp)           # Error: temp is not defined

# 10. Constants (by convention, use uppercase)
PI = 3.14159
MAX_USERS = 100

# 11. Variable Scope
global_var = "I am global"

def my_func():
    local_var = "I am local"
    print(local_var)
    print(global_var)   # can access global variable

my_func()
# print(local_var)      # Error: local_var is not defined outside function

# 12. Swapping Variables
a = 1
b = 2
a, b = b, a             # a is now 2, b is now 1

# 13. Unpacking Collections
data = [10, 20, 30]
x, y, z = data          # x=10, y=20, z=30

# 14. Dynamic Typing
var = 10
var = "Now I'm a string" # variable type can change

# 15. Reserved Words (cannot be used as variable names)
# Examples: if, for, while, class, def, etc.

# 16. Underscore in Variables
_private = "private variable"
var_1 = "valid"
_var = "also valid"
# 1var = "invalid"      # Invalid: starts with a number (commented out)
# my-var = "invalid"    # Invalid: contains a hyphen (commented out)
# for = "invalid"       # Invalid: reserved word (commented out)

# 17. Useful Functions
print(globals())        # shows all global variables
print(locals())         # shows local variables in current scope

# 18. Input from User
user_name = input("Enter your name: ")
print("Hello,", user_name)

# 19. Annotating Variable Types (Python 3.6+)
age: int = 25
name: str = "Bob"
height: float = 5.9

# 20. Summary
# - Variables store data
# - Names must follow rules
# - Types are dynamic
# - Use type() to check type
# - Use del to delete
# - Use input() for user input

# 21. Type Conversions (Type Casting) with Examples

# int to float
a = 7
b = float(a)        # b = 7.0

# float to int (decimal part is removed)
c = 3.99
d = int(c)          # d = 3

# string to int
num_str = "123"
num_int = int(num_str)  # num_int = 123

# string to float
float_str = "45.67"
num_float = float(float_str)  # num_float = 45.67

# int to string
n = 10
n_str = str(n)      # n_str = "10"

# float to string
f = 2.5
f_str = str(f)      # f_str = "2.5"

# bool to int
flag = True
flag_int = int(flag)    # flag_int = 1

# int to bool
zero = 0
zero_bool = bool(zero)  # zero_bool = False

# list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)   # my_tuple = (1, 2, 3)

# tuple to list
my_tuple2 = (4, 5, 6)
my_list2 = list(my_tuple2)  # my_list2 = [4, 5, 6]

# Example prints
print(float(a))
print(int(c))
print(int(num_str))
print(str(n))
print(bool(zero))
print(tuple(my_list))
print(list(my_tuple2))
