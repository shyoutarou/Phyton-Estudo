# Python program to demonstrate
# higher order functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

#HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(shout)
#hi, i am created by a function passed as an argument.
greet(whisper)
