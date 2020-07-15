def alterar_lista(lista):
    lista[1] = 3
    return lista


lista = [2, 4, 6, 8]
# Perceber que, para list's que sao inseridas nos parametros
# da function a list mantem os valores atribuidos dentro
# da function, pois as lists armazenam endereços de memoria

print(alterar_lista(lista))
