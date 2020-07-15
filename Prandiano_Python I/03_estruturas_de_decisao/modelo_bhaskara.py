"""Pseudo-Código
Inicio
    digitar coeficiente_a
    digitar coeficiente_b
    digitar coeficiente_c
    Se a = 0 Então
        Se b != 0 Então
            Imprimir "A equação possui uma única raiz"
            r_um <- -c/b
            Imprimir r_um
        Senão b = 0 Então
            Imprimir "Indeterminação/Singularidade"
            Sair da subrotina
        Fim do Se
    Senão
        delta <- b ** 2 - 4 * a * c
        Se delta >= Então
            r_um <- (- b - delta ** (1 / 2))/(2 * a)
            r_dois <- (- b + delta ** (1 / 2))/(2 * a)
            Imprimir "A equação possui duas raízes"
            Imprimir r_um
            Imprimir r_dois
        Senão delta < 0 Então
            Imprimir "A equação possui raiz imaginária"
            real <- -b / (2 * a)
            imaginaria <- (delta ** (1 / 2))/(2 * a)
            Imprimir real + imaginaria "j"
        Fim do Se
    Fim do Se
Fim
"""

a = float(input("Digite o valor do coeficiente 'a' (a * (x ** 2) + b * x + c = 0) da equação do segundo grau: "))
b = float(input("Digite o valor do coeficiente 'b' (a * (x ** 2) + b * x + c = 0) da equação do segundo grau: "))
c = float(input("Digite o valor do coeficiente 'c' (a * (x ** 2) + b * x + c = 0) da equação do segundo grau: "))

if a == 0:
    if b != 0:
        print("Observações: a equação possui uma única raiz.")
        R1 = - c / b
        print("Valor da raiz = ", R1)
    else:
        print("Observações: Indeterminação / Singularidade")
        quit()
else:
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        print("Observações: a equação possui duas raízes reais.")
        R1 = (- b - (delta ** (1 / 2))) / (2 * a)
        print("Valor da primeira raiz =", round(R1,2))
        R2 = (- b + (delta ** (1 / 2))) / (2 * a)
        print("Valor da segunda raiz =", round(R2,2))
    else:
        print("Observações: a equação possui raiz imaginária.")
        Re = - b / (2 * a)
        print("Valor da parte real (Re) =", round(Re,2))
        Im = ((- delta) ** (1 / 2)) / (2 * a)
        print("Valor da parte imaginária (Im) =", round(Im,2))