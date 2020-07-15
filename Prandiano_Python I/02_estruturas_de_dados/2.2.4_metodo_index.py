a = -1.4142
b = 2
c = -17
d = 27.6514

E = [a, b, c, d]
print(type(E))   # <class 'list'>
print(E)         # [-1.4142, 2, -17, 27.6514]

print(E.index(-17)) # 2
print(E.index(2)) # 1
# print(E.index(27.65)) # Proposital
print(E.index(-1.4142)) # 0

# E = E + 2 # Proposital
E = E + [2]
print(E) # [-1.4142, 2, -17, 27.6514, 2]
print(E.index(2)) # 1
