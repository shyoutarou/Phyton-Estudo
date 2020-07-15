n = input("Digitar o número para ser calculado seu fatorial: ")
n = int(n)
if n < 1:
    quit()
f = 1
for i in range(1, n + 1, 1):
    f = f * i
print("O fatorial do número digitado n=" + str(n) + " é " + str(f) + ".")
