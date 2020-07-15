def categoria(imc):
    categorias = ["Abaixo do Peso", "Peso Normal(Saudável)",
                  "Acima do peso(Sobrepeso)", "Obesidade Grau I(Gordo)",
                   "Obesidade Grau II(Severa)",  "Obesidade Grau III(Mórbido)"]
    if(imc <= 18.5) :
        print(categorias[0])
    elif (imc > 18.5 and imc < 24.9):
        print(categorias[1])
    elif (imc > 24.9 and imc < 29.9):
        print(categorias[2])
    elif (imc > 29.9 and imc < 34.9):
        print(categorias[3])
    elif (imc > 34.9 and imc < 39.9):
        print(categorias[4])
    else :
        print(categorias[5])

def peso():

    while True:
        sexo = input("Digitar: M(masculino) ou F(feminino) \n")
        if sexo != "M" and sexo != "F":
            print("Digite M ou F!")
            continue
        else:
            break

    while True:
        try:
            massa = float(input("Digitar sua massa: "))
            break
        except ValueError:
            print("Digite um número!")
            continue

    while True:
        try:
            altura = float(input("Digitar sua altura: "))
            break
        except ValueError:
            print("Digite um número!")
            continue

    imc = massa / altura ** 2
    print('IMC: {:.2f}'.format(imc))
    categoria(imc)

    if (sexo == "M"):
        peso_ideal = (72.2 * altura) - 57
    else:
        peso_ideal = (62.1 * altura) - 44.7

    print('"O seu peso ideal seria: {:.2f}'.format(peso_ideal))

peso()
