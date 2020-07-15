x = int(input("Digitar o valor de 'x' = "))
y = int(input("Digitar o valor de 'y' = "))

if x >= 0 and x <= 3:
    if y >= 0 and y <= 5:
        folha = "Produto A"
    elif y > 5 and y <= 9:
        folha = "Produto B"
    else:
        folha = "O valor 'y' NÃO está dentro dos limites."
elif x > 3 and x <= 7:
    if y >= 0 and y <= 7:
        folha = "Produto C"
    elif y > 7 and y <= 9:
        if x >= 3 and x <= 5:
            folha = "Produto D"
        elif x > 5 and x <= 7:
            folha = "Produto E"
        else:
            folha = "O valor 'x' NÃO está dentro dos limites."
    else:
        folha = "O valor 'y' NÃO está dentro dos limites."
else:
    folha = "O valor 'x' NÃO está dentro dos limites."

print(folha)