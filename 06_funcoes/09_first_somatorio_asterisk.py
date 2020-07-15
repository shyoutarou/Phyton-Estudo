def somatorio(lista_ou_tupla):
    # Calcular somatorio.
    # Perceber que, foi criada uma variavel auxiliar
    # (somatorio_aux) para NAO coincidir com o nome da function.
    #  Tudo isso, neste caso, pa	ra NAO transrormar esta function
    # em uma funcao de recursivi	dade
    somatorio_aux = 0
    for elemento in lista_ou_tupla:
        somatorio_aux = somatorio_aux + elemento
    return somatorio_aux


fibonacci_parcial = [1, 1, 2, 3, 5, 8]
print(somatorio(fibonacci_parcial))
fibonacci_parcial_dois = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
print(somatorio(fibonacci_parcial_dois))
