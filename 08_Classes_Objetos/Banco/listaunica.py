class ListaUnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class
    def __len__(self):
        return len(self.lista) 
    def __iter__(self):
        return iter(self.lista) 
    def __getitem__(self, p):
        return self.lista[p]
    def indiceValido(self, i):
        return i >= 0 and i < len(self.lista) 
    def adiciona(self, elem):
        if self.pesquisa(elem) == -1: 
            self.lista.append(elem) 
    def remove(self, elem):
        self.lista.remove(elem)
    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError: 
            return -1 

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_class): 
            raise TypeError("Tipo invalido") 
    def ordena(self, chave=None):
        self. lista.sort(key=chave)
