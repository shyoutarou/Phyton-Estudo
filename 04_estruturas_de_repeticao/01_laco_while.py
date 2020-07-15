senha = "54321"
leitura = "   "
while (leitura != senha):
    leitura = input("Digite a  senha: ")
    if leitura == senha:
        print('Acesso liberado')
    else:
        print('Senha incorreta. Tente novamente')

contador = 0
somador = 0
while contador < 5:
    contador = contador + 1
    valor = float(input('Digite o ' + str(contador) + '° valor: '))
    somador = somador + valor

print('Soma = ', somador)
