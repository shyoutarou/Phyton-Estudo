# stringprefix  = "r" | "u" | "ur" | "R" | "U" | "UR" | "Ur" | "uR"

""" r-string
Uma string r é uma string bruta, ela ignora caracteres de escape.
Por exemplo, "\ n" é uma sequência que contém um caractere de nova
linha e r"\ n" é uma sequência que contém uma barra invertida e a
letra n. Normalmente você usaria uma string-r se estivesse passando
a string para outra coisa que usa um monte de caracteres estranhos.
"""
""" f-string
Semelhante à forma como você cria uma string bruta, você pode prefixar 
uma string com a letra “f” para obter uma "f-strings". A letra "f" 
indica que uma seqüência de caracteres é usada para formatação, e são 
realmente a maneira mais simples e prática de formatar strings.
"""

name = 'Fred'
age = 42
print(f'He said his name is {name} and he is {age} years old.')

media = 10 / 2
print('Media: {:.2f}'.format(media))
print('Media: ', media)

print("Olá Mundo!!")  # Olá Mundo!!

print("Apostila" + "Python")  # ApostilaPython
a = 'Programação'
b = 'Python'
c = a + b
print(c)  # ProgramaçãoPython

s = "Python"
# Seleciona os elementos das posições 1,2,3
print(s[1:4])  # yth
# Seleciona os elementos a partir da posição 2
print(s[2:])  # thon
# Seleciona os elementos até a posição 3
print(s[:4])  # Pyth

texto = "Meu texto \n\n\t pulei duas linhas e tabulei!"
print(texto)
"""
Meu texto   

      pulei duas linhas e tabulei!
"""

texto = r"\n não pulou linha"
print(texto)  # \n  nao  pulou   linha
