def add_two(b):
    return 2 + b

print(add_two(4)) # 6

from functools import partial

def add(a, b):
    return a + b

add_two = partial(add, 2)
add_ten = partial(add, 10)

print(add_two(4)) # 6
print(add_ten(4)) # 14

# A partial that grabs IP addresses using
# the `map` function from the standard library.
extract_ips = partial(
    map,
    lambda x: x.split(' ')[0]
)

arquivo = open('nome_errado.txt', 'r', encoding="utf8")
lines = arquivo.read()
print(lines) # Toque Frágil .....
ip_addresses = list(extract_ips(lines))
print(ip_addresses) # ['T', 'o', 'q', 'u', 'e', '', 'F', 'r', 'á', 'g', 'i', 'l' ..