

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')


def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))


def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))


if __name__ == '__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()


def celsius(c=0):
    con1 = c + 273
    con2 = (c * 9.) / 5. + 32
    print(" A conversao em Kelvin: %dK" % con1)
    print(" A conversao em Fahrenheit: %.2fF" % con2)


def kelvin(k=0):
    con3 = k - 273
    con4 = ((k - 273) / 5.) * 9. + 32
    print(" A conversao em Celsius: %.2fC" % con3)
    print(" A conversao em Fahrenheit: %.2fF" % con4)


def fahrenheit(f=0):
    con5 = ((f - 32) / 9.) * 5.
    con6 = ((f - 32) / 9.) * 5. + 273
    print(" A conversao em Celsius: %.2fC" % con5)
    print(" A conversao em Kelvin: %.2fK" % con6)


def janela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('CLS')
    print("  Conversor de Temperaturas: Celsius, Kelvin e Fahrenheit!\n")
    print(" Copyright(c)- Astdarkness(2004)-by Alan Santos Teixeira\n")
    print("============================================================")
    print("        Escolha uma das alternativas e tecle enter")
    print("\n")
    print("        1. Celsius para kelvin e Fahrenheit")
    print("        2. Kelvin para Celsius e Fahrenheit")
    print("        3. Fahrenheit para kelvin e Celsius")
    print("\n")
    print("        4. Sair deste programa")
    print("===========================================================")


def loof():
    while 1:
        # Somente um prompt
        try:
            x = input('> ')
        except:
            # Somente por questão de segurança
            x = 0
        if x == 1:
            celsius(input('Digite um valor em Celsius: '))
        elif x == 2:
            kelvin(input('Digite um valor em Kelvin: '))
        elif x == 3:
            fahrenheit(input('Digite um valor em Fahrenheit: '))
        elif x == 4:
            print("Saindo...")
            break
        else:
            # Se o valor digitado não for 1, 2, 3 ou 4, redesenha a janela
            janela()


def main():
    # Esta é a função principal, que executa as outras
    janela()
    loof()


if __name__ == "__main__":
    # Este bloco de comandos faz com que a função principal main() seja
    # executada somente se o script for executado, não se for importado
    main()

ask = input("Escolha para que escala quer converter a temperatura: Celcius ou Fahrenheit?")

if ask == "Celcius" or ask == "celcius":
    temp1 = input("Qual é a temperatura em Fahrenheit?")
    try:
        Fahr = float(temp1)
    except:
        print("Erro: Coloque um numero para a temperatura")
        quit()

    Celcius = (Fahr - 32) / 1.8
    print("Estão %3.2f graus Celcius" % Celcius)

elif ask == "Fahrenheit" or ask == "fahrenheit":
    temp2 = input("Qual é a temperatura em Celcius?")
    try:
        Cel = float(temp2)
    except:
        print("Erro: Coloque um numero para a temperatura")
        quit()

    Fahrenheit = Cel * 1.8 + 32
    print(" Estão %3.2f graus Fahrenheit" % Fahrenheit)

else:
    print
    "Escolha entre Celcius e Fahrenheit"
