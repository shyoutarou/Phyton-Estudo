# 1. e 2. Digital as somas dos caracteres:
soma_um = int(input ('Digitar a soma do "primeiro" com o "segundo"' + ' caracteres da senha (da esquerda para a direita) = '))
soma_dois = int(input ('Digitar a soma do "segundo" com o "terceiro"' + ' caracteres da senha (da esquerda para a direita) = '))
soma_tres = int(input ('Digitar a soma do "terceiro" com o "quarto"' + ' caracteres da senha (da esquerda para a direita) = '))
soma_quatro = int(input ('Digitar a soma do "quarto" com o "quinto"' + ' caracteres da senha (da esquerda para a direita) = '))
soma_cinco = int(input ('Digitar a soma do "quinto" com o "sexto"' + ' caracteres da senha (da esquerda para a direita) = '))
# obs: quando estou trabalhando com texto, o "+" é um operador de concatenação

print('')
print('OBSERVAÇÃO: NÃO pode existir somas maiores que 19 (dezenove)')
print('')

# 3. Calcular a soma das somas alternando os sinais:
soma = + soma_um - soma_dois + soma_tres - soma_quatro + soma_cinco

# 4. Calcular a divisao do item anterior por dois:
divisao = round(soma / 2 , 0) # A função <round> servirá para garantir pegar sempre um número inteiro após a divisão

# 5. Executar cálculos finais:
calculo_um = + soma_um - divisao
calculo_dois = - soma_dois + calculo_um
calculo_tres = + soma_tres + calculo_dois
calculo_quatro = - soma_quatro + calculo_tres
calculo_cinco = + soma_cinco + calculo_quatro

print('')
print('A senha é: ' + str(int(abs(divisao))) + str(int(abs(calculo_um))) + str(int(abs(calculo_dois))) + str(int(abs(calculo_tres))) + str(int(abs(calculo_quatro))))
