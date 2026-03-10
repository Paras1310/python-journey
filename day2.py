 # TODO: create programs using conditions statements

# * using int() data type to allow for integer numbers:

# * using input() function to take input from the user: 

first_number=int(input("first number: "))
second_number=int(input("second number: "))
third_number=int(input("third number: "))

age = int(input("enter your age: "))

grade=int(input("enter your marks: "))

# ! even and odd program:

if first_number % 2 == 0:
    print(f"{first_number} is even")
else:
    print(f"{first_number} is odd")


# ! age checker:

if age < 13:
    print("child", age)
elif age < 20:
    print("teenager", age)
elif age < 60:
    print("adult", age)
else:
    print("senior", age)

# ! largest number:

if first_number > second_number and first_number > third_number:
    print("first number in largest", first_number)
elif second_number > third_number and second_number > first_number:
    print("second number is largest", second_number)
elif third_number > second_number and third_number > first_number:
    print("third_number is largest",third_number)
else:
    print("all numbers are equal.")

# * in modern way:
largest = max(first_number, second_number, third_number)
print("Largest number is:", largest)


# ? why we use extra elif?
'''
    elif allows us to check another condition if the previous one was false.
'''
# ! grade calculator:

if grade >= 90:
    print("A+",grade)
elif grade >= 80:
    print("A",grade) 
elif grade >= 70:
    print("B",grade) 
elif grade >= 55:
    print("C",grade) 
elif grade >= 40:
    print("D",grade) 
else:
    print("fail",grade)

# ! positive and negative numbers:

if first_number > 0:
    print(f"{first_number} is positive")
elif first_number < 0:
    print(f"{first_number} is negative")
else:
    print("zero")