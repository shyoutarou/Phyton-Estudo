a = 3
b = 4
c = 5

if a==b and b==c:
    tipo_do_triangulo = "equilatero"
elif a==b or b==c or a==c:
    tipo_do_triangulo = "isósceles"
elif a != b and a != c and b!= c:
    tipo_do_triangulo = "escaleno"

perimetro = a + b + c
p = perimetro / 2
area_do_triangulo = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

print("Tipo do triangulo:", tipo_do_triangulo)
print("Àrea do triangulo:", area_do_triangulo)
