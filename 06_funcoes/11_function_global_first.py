def soma_um(num):
    num = num + 1
    print("0 valor da variavel num dentro da function e: " + str(num))
    return num

num = 12
print("0 valor da variavel num ANTES de chamar a function e: " + str(num))
print("0 valor da soma_um e: " + str(soma_um(num)))
print("0 valor da variavel num DEP0IS de chamar a function e: " + str(num))
# Perceber que, a variavel num inserida antes de chamar a
# function soma_um continua com o mesmo valor, isto ocorre,
# pois a variavel trata-se de uma variavel local, ou seja,
# a function cria uma copia da variavel inserida no parametro
