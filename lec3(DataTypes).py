# DATA TYPES
#   Whenever you create a variable in Python, it has a value with a corresponding data type. There are many different data types, such as integers, floats, booleans, and strings.

# 1. Integers
#          Integers are numbers without any fractional part and can be positive (1, 2, 3, ...), negative (-1, -2, -3, ...), or zero (0).

num = 10
print(type(num))

# 2. Floats
#       Floats are numbers with fractional parts. They can have many numbers after decimal.
#  int():- This function can change the data type of a float variable to integer.

pi = 3.14357635176451763
pi2 = 22/7
print(type(pi))

pi = int(pi)
print(pi)

# round() :- It lets you round a number to a specified number of decimal places.

print(round(pi,4))

# Whenever you write an number with a decimal point, Python recognizes it as a float data type.

x = 2.
print(type(x))

# 3. Booleans
#       Booleans represent one of two values: True/1 or False/0. 

num_bool = False
print(type(num_bool))

var = (4>9)
print(var)
print(type(var))

# 'not' keyword:- It changes the value of boolean. not true = false, not false = true

var = not False
print(var)
print(type(var))

# 4. Strings
#       The string data type is a collection of characters (like alphabet letters, punctuation, numerical digits, or symbols) contained in quotation marks. Strings are commonly used to represent text.

name = "Hello! My name is Aashi."
print(type(name))

# len():- It is a function which gives the total length of string. "" are not included in length. And, it also counts the spaces in the string.

print(len(name))

str = ""  #string with length = 0. It is Empty String.
print(len(str))

# NOTE:- If you put a number in quotation marks, it has a string data type.
new_var = "23.33"
print(type(new_var)) 

# float() :- This function try to change any data type to float.

new_var = float(new_var)
print(type(new_var))

var2 = True
print(var2)
var2 = float(var2)
print(var2)
print(type(var2))

# float() can convert data type to float only if possible.

# str2 = "Aashi"
# str2 = float(str2)
# print(str2)            This will throw error.


# CONCATENATION :- Just like you can add two numbers (floats or integers), you can also add two strings. It results in a longer string that combines the two original strings by concatenating them.

first_name = "Aashi"
last_name = "Chauhan"
full_name = first_name + last_name
print(full_name)

# Note that it's not possible to do subtraction or division with two strings.You also can't multiply two strings, but you can multiply a string by an integer.
# Note that you cannot multiply a string by a float. This will throw an error.

str3 = "Apple"*5
print(str3)
