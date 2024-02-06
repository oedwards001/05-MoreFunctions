import math

###############################################################################
# Done: 1. (6 pts)
#
#   In this module, we are going to start the process of making our own
#   calculator. It is going to be a very simple calculator, because the user
#   won't be able to tell it what operation to do. They will only provide it
#   with two numbers and it will print out the answers for all four basic
#   operations (add, subtract, multiply, and divide).
#
#   So first, we are going to need some functions for each of the operations.
#
#   Right below this _TODO_ write four different functions:
#     - add()
#     - subtract()
#     - multiply()
#     - divide()
#
#   Each one should take two parameters (one for each number in the
#   calculation). Each function should then do the respective operation on the
#   two numbers. For add and multiply, the order doesn't matter, but for
#   subtract and divide, assume that the first parameter is the first number
#   and the second parameter is the second number. For example:
#
#   first_param - second_param
#
#   Once each function has done its calculation, it should return the result.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def add(first_param, second_param):
    addition = first_param + second_param
    return addition    
  
def subtract(first_param, second_param):
    subtraction = first_param - second_param
    return subtraction

def multiply(first_param, second_param):
    multiplication = first_param*second_param
    return multiplication

def divide(first_param, second_param):
    division = first_param / second_param
    return division

def power(first_param, second_param):
    powerraise = math.pow(first_param, second_param)
    return powerraise

###############################################################################
# Done6: 2. (8 pts)
#
#   Now we need a function that will act as the control unit. It will ask the
#   user for inputs and call the math functions.
#
#   Write a function called main() that takes no parameters. It should do these
#   things in order:
#     1. Greet the user in some friendly way
#     2. Ask the user for their first input, allow the user to enter the first
#        number, and save it to a variable.
#     3. Ask the user for their second input, allow the user to enter the
#        second number, and save it to a variable.
#     4. Uses those inputs to do all four operations and prints the results
#        back to the user. Do NOT simply do the math here. Use the functions
#        you defined in the first _TODO_.
#     5. Says a friendly goodbye to the user.
#
#   So, if a user gave 6 and 3 as their inputs. Your calculator should return
#   something like this as its results.
#
#   Add: 9
#   Subtract: 3
#   Multiply: 18
#   Divide: 2
#
#   Once you have defined your main() function, make sure you call it to start
#   the ball rolling.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    print("Hello, how are you?")

    number1 = input("number1: ") 
    number1 = int(number1) 
    print(f"Your first number chosen is {number1}.") 
    
    number2 = input("number2: ")
    number2 = int(number2)
    print(f"Your second number chosen is {number2}.")


    addition = add(first_param=number1, second_param=number2) 
    print(f"Add: {addition}") 

    subtraction = subtract(first_param=number1, second_param=number2)
    print (f"Subtract: {subtraction}")

    multiplication = multiply(first_param=number1, second_param=number2)
    print (f"Multiply: {multiplication}")

    division = divide(first_param=number1, second_param=number2)
    print (f"Divide: {division}")

    powerraise = power(first_param=number1, second_param=number2)
    print (f"Power: {powerraise}")

print("Goodbye!")
    
main()
    

###############################################################################
# Done: 3. EXTRA CREDIT (4 pts)
#
#   For this _TODO_, do NOT write your code beneath it. You will be modifying
#   your code above. This is extra credit, so you don't need to complete this
#   _TODO_ to receive full points on this assignment, but you can receive up to
#   4 points of extra credit.
#
#   For some extra credit points, modify your code above to include another
#   math operation. Go through the math module documentation that I gave you in
#   the Session 2 materials, pick one math operation that we haven't used in
#   this class before that uses two numbers as its inputs. Then write a
#   function similar to the ones you created above and add a print statement to
#   your main() function that prints the result of it as well as the other
#   operations you did as a part of this module. Make sure you import the math
#   module on this file (just like I did for your previous exercises) so you
#   will be able to use it. 
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
