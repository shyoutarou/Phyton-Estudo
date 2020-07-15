"""
def mydecoratorfunction(some_function):
    def wrapper_function():
        some_function() # call some_function
    return wrapper_function
"""

def display(str): print(str)

# função a ser decorada passada como argumento
def displaydecorator(funcao):
    # wrap the some_function e estende seu comportamento
    def display_wrapper(str):
        # write code para estender o comportamento de some_function()
        print('Saída:', end=" ")
        funcao(str)
    # retorno da wrapper_function
    return display_wrapper

@displaydecorator
def display(str): print(str)

display('Olá Mundo') # Saída: Olá Mundo

out = displaydecorator(display)
out('Olá Mundo') # Saída: Saída: Olá Mundo
