 # TODO: Create the Programs using input and print the result.

# * using int() data type to allow for integer numbers:

# * using float() data type to allow for decimal numbers:

# * using input() function to take input from the user: 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# ! addtion of two numbers:

# * addition of two numbers by using the ( + ) arithmetic operator:
result = num1 + num2

print("The sum of", num1, "and", num2, "is:", result)

# ! average of three numbers:


# * average of three numbers by using the ( +, / )  arithmetic operators:
average = (num1 + num2 + num3) / 3
print("The average of", num1, ",", num2, "and", num3, "is:", average)

# ? why we use float() instead of int() in the average program?
''' 
    we use float() instead of int() in the average program 
    because the average of three numbers can be a decimal number.
'''

# ! future age calculator:

current_age = int(input("Enter your current age: "))
years_to_add = 5

# * future age by using the ( + )  arithmetic operators:
future_age = current_age + years_to_add

print("In", years_to_add, "years, you will be", future_age, "years old.")

''' 
    we can also take the number of years to add
    which make year to add dynamic instead of static.
'''

# ! temperature converter: Celsius to Fahrenheit:

# * conversion from Celsius to Fahrenheit by using the ( * )  arithmetic operators:

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


# ! simple interest calculator:

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))  
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

# ! square of a number:

number = float(input("Enter a number: "))

# * square of a number by using the ( ** )  arithmetic operators:
square = number ** 2

print("Square of", number, "is:", square)

# ! cube of a number:

number = float(input("Enter a number: "))

# * cube of a number by using the ( ** )  arithmetic operators:
cube = number ** 3

print("Cube of", number, "is:", cube)