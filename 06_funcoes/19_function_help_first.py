def gerar_matrix(I, J):
    """
		Esta função auxilia a criação de uma matrix.
		:param I: Número total de linhas da matrix.
		:param J: Número total de colunas da matrix.
		:return: Matrix com os valores dos elementos inseridos
		pelo usuario.
    """
    matrix = []
    for i in range(1, I + 1, 1):
        linha = []
        # 0 %i, i significa int e NAO trata-se do i (indice)
        #  da matrix NAO confundir!
        for j in range(1, J + 1, 1):
            a_i_j = float(input("Digitar c valor do elemento "
                                "a(%i, %i) : " % (i, j)))
            linha.append(a_i_j)
        matrix.append(linha)
    return matrix


print(help(gerar_matrix))
