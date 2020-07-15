from nome import Nome
from telefone import Telefone
from listaunica import ListaUnica

class Telefones(ListaUnica):
    def __init__(self):
        super().__init__(Telefone)

class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):
            raise TypeError("nome deve ser instância da classe Nome")
        self.__nome = valor

    def pesquisaTelefone(self,telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefone



"""
nome = Nome("Ric")
A = DadoAgenda(nome)
"""