def soma_sete(num):
    acrescimo = 7
    num = num + acrescimo
    print("0 valor da variavel num dentro da function " + str(num))
    return num


num = 12
print("0 valor da variavel num ANTES de chamar a function e: " + str(num))

print("0 valor	da	soma_um e : " + str(soma_sete(num)))
print("0 valor	da variavel num DEPOIS de chamar a function	e:	" + str(num))
#	Perceber que, a	variavel num inserida antes de
#	function soma_sete continua com o mesmo valor, isto
#	pois a variavel trata-se de	ima variavel local,
#	a function cria uma copia da variavel inserida
# print(acrescimo)  # Proposital
#	Perceber que, a	variavel acrescimo e uma variavel
#	da function soma_sete e NAO	do	script geral!
