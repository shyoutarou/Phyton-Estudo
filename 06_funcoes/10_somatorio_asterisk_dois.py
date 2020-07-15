# Perceber que, foi adicionado um asterisco
# precedendo o parametro lista_ou_tupla

def somatorio_asterisco_dois(*lista_ou_tupla):
    # Perceber que, foi criado uma variavel auxiliar logo
    # abaixo para que, NAO coincida com o nome da funcao
    somatorio_aux = 0
    for elemento in lista_ou_tupla:
        somatorio_aux = somatorio_aux + elemento
    return somatorio_aux
# Quando o asterisco e inserido antes do parametro lista__ou_tupla,
# NAO e necessario inserir a lista ou tupla dentro de
# colchetes ou parentesis:
print(somatorio_asterisco_dois(1, 2, 3, 4, 5))
# Faça o teste removendo o asterisco do paremtro da funcao
