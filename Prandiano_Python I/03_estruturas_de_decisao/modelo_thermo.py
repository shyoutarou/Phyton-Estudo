escala_de = input("Digite a escala a ser convertida (Celsius/Fahrenheit/Kelvin): ")
escala_de = escala_de.upper()
valor_da_temperatura = float(input("Digite o 'Valor da Temperatura': "))
escala_para = input("Digite a escala na qual o valor deve ser convertido (Celsius/Fahrenheit/Kelvin): ")
escala_para = escala_para.upper()

if escala_de == "KELVIN" and escala_para == "CELSIUS":
    Tk = valor_da_temperatura
    Tc = Tk - 273.15
    print("A temperatura em Celsius (Tc) =", round(Tc, 2),"oC")
elif escala_de == "CELSIUS" and escala_para == "KELVIN":
    Tc = valor_da_temperatura
    Tk = Tc + 273.15
    print("A temperatura em Kelvin (Tk) =", round(Tk, 2),"K")
elif escala_de == "FAHRENHEIT" and escala_para == "CELSIUS":
    Tf = valor_da_temperatura
    Tc = (5 / 9) * Tf - 160 / 9
    print("A temperatura em Celsius (Tc) =", round(Tc, 2),"oC")
elif escala_de == "CELSIUS" and escala_para == "FAHRENHEIT":
    Tc = valor_da_temperatura
    Tf = (9 / 5) * Tc + 32
    print("A temperatura em Fahrenheit (Tf) =", round(Tf, 2), "oF")
elif escala_de == "KELVIN" and escala_para == "FAHRENHEIT":
    Tk = valor_da_temperatura
    Tc = Tk - 273.15
    Tf = (9 / 5) * Tc + 32
    print("A temperatura em Fahrenheit (Tf) =", round(Tf, 2), "oF")
elif escala_de == "FAHRENHEIT" and escala_para =="KELVIN":
    Tf = valor_da_temperatura
    Tc = (5 / 9) * Tf - 160 / 9
    Tk = Tc + 273.15
    print("A temperatura em Kelvin (Tk) =", round(Tk, 2), "K")
else:
    print("")
