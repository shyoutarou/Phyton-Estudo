i = input("Digitar o valor inicial(i): ")
i = int(i)
n = input("Digitar o valor final(n): ")
n = int(n)
passo = 1
p = 1
for i in range(1, n + 1, passo):
    p = p * i
# Perceber que o produtorio para i = 1
# e passo = 1 possui o mesmo resultado fatorial
print("Produtório: " + p)
