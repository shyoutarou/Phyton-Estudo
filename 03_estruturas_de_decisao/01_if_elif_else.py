valor = int(input("Qual sua idade?"))

if valor < 6:
    print("Que coisa fofa!")
elif valor < 18:
    print("Você ainda não pode dirigir!")
elif valor > 60:
    print("Você está na melhor idade!")
else:
    print("Você é o cara!")

# Pass
# Sem muita utilidade, serve como variável de teste
# e tem valor equiparado a null:

for num in range(1,6):
    if num==3:
        pass
    else:
        print ("Num =  {} ".format(num))

