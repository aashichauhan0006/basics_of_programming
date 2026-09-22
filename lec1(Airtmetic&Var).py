#WELCOME TO PROGRAMMING

#1. ARITHMETIC & VARIABLES

#    PRINTING
#        " " = Quotation.
#        ( ) = Parantheses.
#NOTE:- we cannot add more than one quotations in a parantheses. 

print("Hello! World.")  

#2. ARITHMETIC
#       EXPONENTS = Power or Root. e.g - 3**2 = (3*3) = 9, 3**3 = (3*3*3) = 27. 
#       PEMDAS(Parantheses > Exponents > Multiply or Divide > Add or Subtract)

print(((1+3)*(9-2)/2)**2)

#3. VARIABLES :- These are symbolic name or reference that points to an object stored in computer's memory.

test_var1 = 5+4

print(test_var1)

test_var2 = "Aashi"
print(test_var2)

test_var3 = 3*2
test_var4 = 4/2

print(test_var3 + test_var4)

#Variable names are ideally short and descriptive. They also need to satisfy several requirements:

#They can't have spaces (e.g., test var is not allowed)
#They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
#They have to start with a letter or underscore (e.g., 1_var is not allowed)

#Manipulting Variables

# Set the value of a new variable to 3
my_var = 3

# Print the value assigned to my_var
print(my_var)

# Change the value of the variable to 100
my_var = 100

# Print the new value assigned to my_var
print(my_var)

#NOTE:- Variables stores the latest value assigned to them.

my_var = my_var + 3
my_var += 3                 #both have same meaning

print(my_var)

#DEBUGGING :- One common error when working with variables is to accidentally introduce typos. For instance, if we spell hours_per_day as hours_per_dy, Python will error with message NameError: name 'hours_per_dy' is not defined.



