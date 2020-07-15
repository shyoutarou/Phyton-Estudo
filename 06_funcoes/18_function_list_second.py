def gerar_matrix(I, J, matrix):
    matrix = []
    for i in range(1, I + 1, 1):
        linha = []
        # 0 %i, i significa int e NAO trata-se do i (indice)
        #  da matrix NAO confundir!
        for j in range(1, J + 1, 1):
            a_i_j = float(input("Digitar c valor do "
                                "elemento "
                                "a(%i, %i) : " % (i, j)))
            linha.append(a_i_j)
        matrix.append(linha)
    return matrix


I = int(input("Digitar o valor do 'Numero Total de Linhas da Matrix': "))
J = int(input("Digitar o valor do 'Numero de Colunas da Matrix': "))
matrix = []
print(gerar_matrix(I, J, matrix))
print(type(matrix))
