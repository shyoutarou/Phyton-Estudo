num_iter = int(input("Digitar o número máximo da sequência de Farey = "))
num_iter = num_iter + 1

def farey(n, asc=True):
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n - 1, n
    i = 1
    print("%d/%d" % (a, b) + ", ", end='')
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b) / d)
        a, b, c, d = c, d, k * c - a, k * d - b

        if a == b :
            print("%d/%d" % (a, b), end=' ')
        else :
            print("%d/%d" % (a, b) + ", ", end='')
        i += 1


def farey_divisao(n, asc=True):
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n - 1, n
    i = 1
    print('{:.2f}'.format(a / b) + ", ", end='')
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b) / d)
        a, b, c, d = c, d, k * c - a, k * d - b

        if a == b:
            print('{:.2f}'.format(a / b), end=' ')
        else:
            print('{:.2f}'.format(a / b) + ", ", end='')
        i += 1

for j in range(1, num_iter):
    print('F' + str(j) + ' = ', end='')
    print('{ ', end=' ')
    farey(j)
    print(' }')

for j in range(1, num_iter):
    print('F' + str(j) + ' = ', end='')
    print('{ ', end=' ')
    farey_divisao(j)
    print(' }')

"""
As sequências de Farey são nomeadas a partir do geólogo Britânico John Farey, 
que teve suas cartas sobre essas sequências publicadas na revista Philosophical 
Magazine em 1816. Farey conjecturou, sem apresentar provas, que cada novo termo 
na expansão de uma sequência de Farey é a mediante de seus vizinhos. A carta de 
Farey foi lida por Cauchy, que forneceu uma prova em seus Exercices de mathématique, 
e atribuiu este resultado a Farey. Na realidade, outro matemático, Charles Haros, 
havia publicado resultados similares em 1802 que não eram conhecidos nem por Farey 
ou por Cauchy.[2] Portanto foi um acidente histórico que ligou o nome de Farey a 
essas sequências. Este é um exemplo da Lei de Stigler.

As sequências de Farey de ordem 1 até 8 são : 
F1 = { 0/1, 1/1 }
F2 = { 0/1, 1/2, 1/1 }
F3 = { 0/1, 1/3, 1/2, 2/3, 1/1 }
F4 = { 0/1, 1/4, 1/3, 1/2, 2/3, 3/4, 1/1 }
F5 = { 0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1 }
F6 = { 0/1, 1/6, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 5/6, 1/1 }
F7 = { 0/1, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 1/1 }
F8 = { 0/1, 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8, 1/1 } 

Order   Count
1       2        F1 = {0/1,                                                                                                          1/1}
2       3        F2 = {0/1,                                                   1/2,                                                   1/1}
3       5        F3 = {0/1,                               1/3,                1/2,                2/3,                               1/1}
4       7        F4 = {0/1,                     1/4,      1/3,                1/2,                2/3,      3/4,                     1/1}
5       11       F5 = {0/1,                1/5, 1/4,      1/3,      2/5,      1/2,      3/5,      2/3,      3/4, 4/5,                1/1}
6       13       F6 = {0/1,           1/6, 1/5, 1/4,      1/3,      2/5,      1/2,      3/5,      2/3,      3/4, 4/5, 5/6,           1/1}
7       19       F7 = {0/1,      1/7, 1/6, 1/5, 1/4, 2/7, 1/3,      2/5, 3/7, 1/2, 4/7, 3/5,      2/3, 5/7, 3/4, 4/5, 5/6, 6/7,      1/1}
8       23       F8 = {0/1, 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8, 1/1}
 
"""
