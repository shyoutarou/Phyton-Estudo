massa = float(input("Digite a massa (kg) = "))
altura = float(input("Digite a altura (m) = "))

imc = massa / (altura ** 2)
print("O Índice de Massa Corporal (IMC) é de: " + str(round(imc, 2)))

if imc <= 18.5:
    categoria = "Abaixo do Peso."
elif imc > 18.5 and imc <= 24.9:
    categoria = "Peso Normal (Saudável)."
elif imc > 24.9 and imc <= 29.9:
    categoria = "Acima do Peso (Sobrepeso)."
elif imc > 29.9 and imc <= 34.9:
    categoria = "Obesidade Grau I (Gordo)."
elif imc > 34.9 and imc <= 39.9:
    categoria = "Obesidade Grau II (Severa)."
elif imc > 39.9:
    categoria = "Obesidade Grau III (Mórbida)."

print("")
print("RESULTADO(S)")
print("A categoria é: ", str(categoria))
