class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r', encoding="utf8")
        self.lines = []
    def read(self):
        self.lines = [line for line in self.file]
    def count(self):
        return len(self.lines)

arquivo = LineCounter('nome_errado.txt')
print(arquivo.lines) # []
print(arquivo.count()) # 0

# The lc object must read the file to
# set the lines property.
arquivo.read()
# The `lc.lines` property has been changed.
# This is called changing the state of the lc
# object.
print(arquivo.lines) # 'Toque Frágil (Walter Franco)\n', '===
print(arquivo.count()) # 7
