def function():
    varl = 37
    var2 = 16
    var3 = 25
    return varl, var2, var3


# Perceber que, a function retorna uma tupla
print(function()) #(37, 16, 25)
x, y, z = function()
print(x) # 37
print(y) # 16
print(z) # 25
