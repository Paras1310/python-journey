 # TODO: LEARN Core Basics 

# ! Understand clearly:

# ? What is a variable?
''' 
    variables are the containers that use to store the value (data) in memory.
    variables are the name that we give to the memory location where we store the data.
    variables are defined by using the assignment operator (=) 
    variables name on the left side and the value on the right side.
    variables are mutable, meaning their values can be changed after they are created.
    variables can store different types of data such as numbers, strings, lists, etc.
'''
# * rules of variables:

'''
    Must start with a letter (a-z, A-Z) or an underscore (_).
    Cannot start with a number (0-9).
    Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
    Are case-sensitive (age, Age, and AGE are three different variables).
    Cannot be Python reserved keywords (like if, for, while, class).
'''

# * types of variables:
'''
   # ! 1. Global variable: 
        a variable that is defined outside of any function and can be accessed from anywhere in the code.
   # ! 2. Local variable: 
        a variable that is defined inside a function and can only be accessed within that function.
'''

# ? What is print() and input()?
'''

# ! print():
              print() is a built-in function in Python that is used to display output to the console. 
              It can take multiple arguments and will print them all on the same line, 
              separated by a space by default.

" syntax: print("Hello, World!") "  Output: Hello, World!
          

# * different ways to use print():

1. seperate multiple arguments with a comma:
 
        name = "Alice"
        age = 30
        print("Name:", name, "Age:", age)
        # Output: Name: Alice Age: 30

2. use the end parameter to change the default newline character:

        print("Hello", end=" ")
        print("World!") 
        # Output: Hello World!

3. use the sep parameter to change the default separator between arguments:

        print("Python", "is", "fun", sep="-")
        # Output: Python-is-fun



# ! input():
              input() is a built-in function in Python that is used to take input from the user. 
              It reads a line of text from the console and returns it as a string. 
              You can also pass a prompt string to input() to display a message to the user,
              before they enter their input.

" syntax: variable = input("Optional prompt message: ") "

# * different ways to use input():

1. taking input without a prompt:

        name = input()
        print("Hello, " + name + "!")
        # If the user enters "Alice", the output will be: Hello, Alice!

2. taking input with a prompt:
        age = input("Please enter your age: ")
        print("You are " + age + " years old.")
        # If the user enters "30", the output will be: You are 30 years old.    

3. taking input and converting it to a different data type:
        
        age_str = input("Enter your age: ")
        # Convert the string input to an integer
        age = int(age_str) 
        print("You are", age, "years old.")

4. taking integer input directly:

        age = int(input("Enter your age: "))
        print("You are", age, "years old.")

5. taking float input directly:

        height = float(input("Enter your height in meters: "))
        print("Your height is", height, "meters.")

6. taking multiple inputs in one line:

        name, age = input("Enter your name and age separated by a space: ").split()
        print("Name:", name)
        print("Age:", age)


'''

# ? What is int(), float(), str()

'''
# ! int():
             int() is a built-in function in Python that is used to convert a value to an integer data type. 
             It can take a string or a number as an argument and will return.
             the integer representation of that value.
             
" syntax: int(value) "

# * examples of int():

             # converting a string to an integer
             age_str = "30"
             age = int(age_str)
             print(age)  # Output: 30
          
# ! float():
             float() is a built-in function in Python that is used to convert a value.
             to a floating-point number (decimal).
" syntax: float(value) "
# * examples of float():

             # converting a string to a float
             height_str = "1.75"
             height = float(height_str)
             print(height)  # Output: 1.75
             
# ! str():
             str() is a built-in function in Python that is used to convert a value to a string data type.
             It can take a number, a list, a tuple, or any other data type as an argument and will return the string representation of that value.
" syntax: str(value) "
# * examples of str():  

             # converting an integer to a string
             age = 30
             age_str = str(age)
             print(age_str)  # Output: "30"
             
             # converting a float to a string
             height = 1.75
             height_str = str(height)
             print(height_str)  # Output: "1.75"
             
             # converting a list to a string
             my_list = [1, 2, 3]
             list_str = str(my_list)
             print(list_str)  # Output: "[1, 2, 3]"
             
'''
