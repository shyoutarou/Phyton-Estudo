#Tipo de set que pode ter valores repetidos, mas tem uma
# palavra-chave única atribuída a cada dado
ano_nasc = {"Pitágoras": -568,
            "Euclides": -329,
            "Eudoxo": -312}

print(type(ano_nasc))

ano_nasc["Arquimedes"] = -287
print(ano_nasc)

print(ano_nasc["Euclides"])

del ano_nasc["Pitágoras"]

ano_nasc["Ptolomeu"] = 112

ano_nasc.keys()
print(ano_nasc.keys())

ano_nasc.values()
print(ano_nasc)

print("Eudoxo" in ano_nasc)
print("Newton" in ano_nasc)

ano_nasc["Leibniz"] = [35, 24, -63]
print(ano_nasc)
