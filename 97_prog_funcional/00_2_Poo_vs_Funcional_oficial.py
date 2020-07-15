def LineCounter(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

arquivo  = LineCounter('nome_errado.txt')
print(count(arquivo)) # 7
print(arquivo) # ['Toque Frágil (Walter

print(count(arquivo)) # 7
print(arquivo) # ['Toque Frágil (Walter
