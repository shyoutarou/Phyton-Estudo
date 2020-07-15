# Python program to illustrate
# nested functions
def function_outer_enclosing(msg):

   def function_inside_nested():
      print (msg)

   function_inside_nested()

function_outer_enclosing('Hello') # Hello

def function_outside():
  msg = 'Hi'
  def function_inside():
      msg = 'Hello'
      print (msg) # Hello
  function_inside()
  print (msg) # Hi

function_outside()

def outerFunction():
  msg = 'Hi'
  def innerFunction():
      nonlocal msg
      msg = 'Hello'
      print (msg) # Hello
  innerFunction()
  print (msg) # Hello

outerFunction()


obj = outerFunction()  #binding the function to an object
del outerFunction  #deleting the outer function
#this returns error as the function is deleted
# NameError: name 'outerFunction' is not defined
outerFunction()
obj()
"""
Hello
Hello
"""
