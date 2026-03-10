 # TODO: Conditional statments

# ! Coditional Statements make decision or execute multiple block of codes.
# ! based on conditions is TRUE or FALSE.

# ? what is if statement?
'''
    if statement was core control flow mechanism used for decision-making.
    It allows a program to execute a specific block of code based on condition
    true.
'''

# * working of if statement
'''
    The if statement evaluates a logical condition (or boolean expression). 

    If the condition is True, the indented code block following the 
    if statement is executed.

    If the condition is False, the indented code block is skipped,
    and the program continues with the next unindented line of code.
'''

# * syntax: 
''' 
     if condition:
        # Code to execute if the condition is True
            statement_1
            statement_2
        # Execution continues here after the if block

# ! Key points of the syntax:

    The if keyword is followed by the condition.
    A colon (:) marks the end of the if line.
    The statements within the if block must be indented consistently 
    (usually four spaces).
'''

'''
# * example

    age = 20
    if age >= 18:
       print("You are an adult") # This line is indented and will execute
       print("You can vote")    # This line is also indented and will execute

'''

# ? what is if-else statemnt?
'''
    A Python if-else statement is a control flow structure that allows
    a program to make decisions and execute specific blocks of code based on
    whether a given condition is True or False.

    In this we use two block of code if one false another is true.
'''

# * working of if-else statement
'''
    1.Condition Evaluation: The program first evaluates the condition within the if 
      statement. This condition is a Boolean expression (or "truthy" value) that results
      in either True or False.

    2.Execution Branching: 
      1. If the condition is True, the code block immediately following the if statement 
         (the "if block") is executed, and the else block is skipped.
 
      2. If the condition is False, the if block is skipped, and the code block following the else statement
         (the "else block") is executed.

    3.Continuation: After one of the blocks runs, the program continues with the next statement after 
      the entire if-else structure.
'''

# * syntax: 
'''
   if condition:
       # Code to execute if the condition is True
   else:
       # Code to execute if the condition is False


# ! Key points of the syntax:


'''

# * example: 
'''
    age = 25

    if age >= 18:
        print("You are eligible to vote.") # This code runs because the condition is True
    else:
        print("You are not eligible to vote.")

'''

# ? what is if elif else statement?
'''
    The if, elif, and else statements in Python are conditional statements used to control 
    the flow of a program by making decisions based on whether a condition is True or False.
    They allow the program to execute specific blocks of code out of a series of alternatives.

    we can make multiple conditions
'''

# * working of if-elif-else
'''
    if statement: The initial check. The code block following if is executed only if its condition is True.

    elif statement: Short for "else if," elif is used to check an alternative condition if the preceding if 
                    (and any other elif) conditions were False. You can have multiple elif blocks.

    else statement: The "catch-all" or default option. The code block following else is executed 
                    if and only if all preceding if and elif conditions in the sequence are False.
'''

# * syntax:
'''
    if condition:
       # Code to execute if the condition is False
    elif contition:
       # Code to execute if the condition is True
    else:
       # Code to execute if the condition is False

# ! Key Points

    1.Only one block of code within an if-elif-else chain will be executed.
    2.The if part is mandatory, but elif and else parts are optional.
    3.Using elif is more efficient than multiple separate if statements for mutually exclusive conditions, 
      as it stops checking once a True condition is found. 
'''

# * example
'''
    age = 25

    if age <= 12:
        print("Child.")
    elif age <= 19:
        print("Teenager.")
    elif age <= 35:
        print("Young adult.")
    else:
        print("Adult.")

'''

# ? what is Comparison / relational Operators?
'''
    Python comparison operators, also known as relational operators, 
      are symbols that compare two values and return a Boolean result: either True or False. 
    
    They are fundamental to controlling the flow of a program, such as in if statements and loops,
      by helping the program make decisions based on conditions. 
'''

# * types of comparison operators
'''
    == (Equal to) and != (Not equal to): 
                                         Check if values are the same or different.

    > (Greater than) and < (Less than):
                                         Compare numerical magnitude or alphabetical order.

    >= (Greater than or equal to) and <= (Less than or equal to):
                                         Combine comparisons with equality. 
'''

# ! Key Characteristics
'''
    1. Boolean Output: Operators always return True or False.
    2. Data Type Comparison: These operators work on numbers, strings (lexicographical order), and, as detailed in, cannot be used between incompatible types like strings and integers without triggering a TypeError.
    3. Operator Chaining: Python allows chaining, such as 2 < x < 10.
    4. Equality vs. Identity: While == compares values, the is operator evaluates if two objects are the same in memory.
'''

# * example
'''
    number = int(input("enter value"))

       if number >= 0:
           print("positive")
       else:
           print("negative")
    
'''

# ? what is Modulus operator % ?
'''
    The Modulo operator (%) is an arithmetic operator that returns the remainder of a division operation. 
      It is a simple yet powerful tool used with numeric types 
       (integers and floating-point numbers) in a wide range of programming tasks.
'''

# * working of module operator
'''
    The syntax for the modulo operator is a % b, where a is the dividend and b is the divisor. 
      The result is the value left over after a is divided by b as many times as possible 
        in a whole number fashion. 
'''

# ! Example 1: Positive Integers
'''
    print(10 % 3)
    # Output: 1 
    # (10 divided by 3 is 3 with a remainder of 1)
'''

# ! Example 2: When divisible evenly
'''
    print(12 % 3)
    # Output: 0
    # (12 divided by 3 is 4 with no remainder)
'''
# ! Example 3: Larger Dividend vs. Divisor
'''
    print(2 % 6)
    # Output: 2
    # (2 divided by 6 is 0 with a remainder of 2)
'''

# * Key Characteristics and Uses
'''

# ! Sign of the Result: 
                        In Python, the sign of the modulo result always takes the sign of the divisor 
                        (the second operand).

                                  print(-10 % 3)  # Output: 2 (sign of 3 is positive)
                                  print(10 % -3)  # Output: -2 (sign of -3 is negative)

# ! Floating-Point Numbers:
                        The modulo operator also works with floats, returning a floating-point remainder.

                                  print(7.5 % 2.5)
                                     # Output: 0.0
                                  print(3.14 % 0.7)
                                     # Output: 0.34

# ! Checking Even or Odd Numbers: 
                         One of the most common uses is to check for divisibility. 
                         A number is even if the remainder when divided by 2 is 0.


                                  number = 14
                                  if number % 2 == 0:
                                      print("Even")
                                  else:
                                      print("Odd")


# ! Cyclic Operations:
                        Modulo is essential for implementing "clock arithmetic" or cycling through a 
                         specific range of values, such as days of the week or elements in a list.


# ! Error Handling:
                        Attempting a modulo operation with a divisor of zero will raise a ZeroDivisionError. 

'''