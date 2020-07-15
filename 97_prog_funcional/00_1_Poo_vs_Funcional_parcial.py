class LineCounter:
    def __init__(self, filename):
        with open(filename, 'r', encoding="utf8") as file:
            self.lines = [line for line in file]
    def count(self):
        return len(self.lines)

arquivo = LineCounter('nome_errado.txt')

print("Linhas: " + str(arquivo.count())) # Linhas: 7
print(arquivo.lines) # ['Toque Frágil (Walter mmm

print("Linhas: " + str(arquivo.count())) # Linhas: 7
print(arquivo.lines) # ['Toque Frágil (Walter

