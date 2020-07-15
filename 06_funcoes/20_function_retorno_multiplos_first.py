def function():
    varl = 37
    var2 = 16
    return varl, var2


# Perceber que, a function retorna uma tupla.
print(function()) #(37, 16)

x, y = function()
print(x) # 37
print(y) # 16

z = function()
print(z) #(37, 16)
