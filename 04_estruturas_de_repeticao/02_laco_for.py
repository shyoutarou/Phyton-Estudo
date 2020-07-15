S = 0
for x in range(1, 20, 3):
    S = S + x

print('Soma: ' , S) # Soma =  70

Lista_notas = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
soma = 0
for nota in Lista_notas:
    soma = soma + nota
    media = soma / len(Lista_notas)

print('Media: {:.2f}'.format(media)) # Media: 7.45
