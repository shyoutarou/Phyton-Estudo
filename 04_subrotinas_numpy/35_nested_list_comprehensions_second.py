"""
Quando não se tem experiência com list comprehensions, estas são um pouco difícies de entender.
A execução dos "for's" das list comprehensions são executados de acordo com a aordem na qual
esses são organizados da estrutura (list compreensions) e, os operadores condicionais
("and" ou "or") são colocados no final conforme feito anteriormente.
"""

# lineararizar uma lista de tuplas
lista_de_tuplas = [(1, 2, 4, "a"),
                   (8, 16, "b", 32),
                   (64, "c", 128, 256)]

k = [x for tupla in lista_de_tuplas for x in tupla]

print(k)

"""
Perceber que, a ordem das expressões dos "for's" seria a mesma se você escrevesse 
uma estrutura de repetição aninhada ao invéss de list comprehensions
"""

linearizado = []

for tupla in lista_de_tuplas:
    for x in tupla:
        linearizado.append(x)

"""
Muitos níveisde aninhamento podem ser arbitrados, porém, em geral, qunado usa-se
mais de três níveis de anunhamento, deve-se suspeitar da estrutura que necessita 
formar, ou seja, compensa repensar se este é o melhor caminho pradesenvolver, 
pois, na verdade, a estrutura é quem pode estar equivocada. É conveniente saber
distinguir a sintaxe acima de uma list comprehensions, ambas válidas:
"""

m = [[x for x in tupla] for tuple in lista_de_tuplas]

print(m)
