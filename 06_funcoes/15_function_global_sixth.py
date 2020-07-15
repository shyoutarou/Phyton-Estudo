def limite_do_palete(qtde_de_cxs):
    global largura, comprimento
    comprimento = comprimento + 2

    k = 32

    largura = largura + \
              2 * qtde_de_cxs - comprimento
    return k


largura = 92
comprimento = 100
qtde_de_cxs = 3
limite_do_palete(qtde_de_cxs)
print(largura)
teste = limite_do_palete(qtde_de_cxs)
print(teste)
