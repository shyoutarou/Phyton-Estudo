import time as time

num_iter = int(input("Digitar o valor do número máximo para a sequência de Fibonacci = "))

tempo_inicio = time.time()
#tempo_inicio_CPU = time.clock()   #ABSOLETO
tempo_inicio_CPU = time.process_time()
tempo_inicio_CPU_2 = time.perf_counter()

# f(0)
f = []
f.append(0)
print(f)

# f(1)
f.append(1)
print(f)

"""
f(n + 2) = f(n) + f(n + 1)
for n in range(0, num_iter - 2, 1)
    f.append(f[n] + f[n + 1] )
"""

n = 0
while n <= num_iter - 3:
    f.append(f[n] + f[n + 1])
    n = n + 1

print(f)

# Imprimir último termo de f
print(f[-1])

# Outra forma:
print(f[len(f) - 1])

tempo_fim = time.time() - tempo_inicio
print("O tempo de execução da aplicação é", tempo_fim, "s")

tempo_fim_CPU_2 = time.perf_counter() - tempo_inicio_CPU_2
print("O tempo de execução da CPU é", tempo_fim_CPU_2)

tempo_fim_CPU = time.process_time() - tempo_inicio_CPU
print("O tempo de execução da CPU é", tempo_fim_CPU)





