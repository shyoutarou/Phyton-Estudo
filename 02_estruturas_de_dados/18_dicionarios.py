# DICIONARIOS

D = {"arroz": 17.30, "feijao": 12.50, "carne": 23.90, "alface": 3.40}

# {'arroz': 17.3, 'feijao': 12.5, 'carne': 23.9, 'alface': 3.4}
print(D)
print(D["carne"])  # 23.9
# print(D("tomate"))

D["arroz"] = 25.0
D["feijao"] = 8.80
# {'arroz': 25.0, 'feijao': 8.8, 'carne': 23.9, 'alface': 3.4}
print(D)

#del D["alface"]
# {'arroz': 25.0, 'feijao': 8.8, 'carne': 23.9}
#print(D)

# dict_keys(['arroz', 'feijao', 'carne', 'alface'])
print(D.keys())

# dict_values([25.0, 8.8, 23.9, 3.4])
print(D.values())
print(len(D)) # 4

# dict_items([('arroz', 25.0), ('feijao', 8.8), ('carne', 23.9), ('alface', 3.4)])
print(D.items())

D = {"arroz": 17.30, "feijao": 12.50, "carne": 23.90, "alface": 3.40}

D.pop("alface")
print(D)  # {'arroz': 17.3, 'feijao': 12.5, 'carne': 23.9}
print(D.get("arroz"))  # 17.3

a = {"aaa": 10, "bbb": 20}
b = {"ddd": 40, "eee": 50}
a.update(b)
# {'aaa': 10, 'bbb': 20, 'ddd': 40, 'eee': 50}
print(a)

# Conversão list para dicionario
d1 = ['aaa', 'bbb', 'ccc']
d2 = ['1', '2', '3']

lista = list(zip(d1, d2))
#  [('aaa', '1'), ('bbb', '2'), ('ccc', '3')]
print(lista)

dicio = dict(zip(d1, d2))
# {'aaa': '1', 'bbb': '2', 'ccc': '3'}
print(dicio)

print(dicio.get("aaa"))  # 1
print(dicio.get("1"))  # None
print(dicio.get("kkkk", "não existe"))  # não existe

print(dicio.pop("aaa"))  # 1
print(dicio.pop("kkkk", "não existe"))  # não existe

Dx = {2: "carro", 3: [4, 5, 6], 7: ('a', 'b'), 4: 173.8}
print(Dx[7])  #  ('a', 'b')

