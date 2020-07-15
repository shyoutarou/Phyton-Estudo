# Imperative
n, num_elements, s = 1, 0, 0
while num_elements < 10:
    if n**2 % 5 == 0:
        s += n
        num_elements += 1
    n += 1

print(s) # 275

# Functional
soma = sum(list(filter(lambda x: x**2 % 5 == 0, range(1, 100)))[:10])
print(s) # 275