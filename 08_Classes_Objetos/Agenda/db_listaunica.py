from listaunica import ListaUnica
from nome import Nome
from tipo_telefone import TipoTelefone
from telefone import Telefone

class DBListaUnica(ListaUnica):
    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.apagados = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        self.apagados = []


class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_


class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_


class DBTelefone(Telefone):
    def __init__(self, numero, tipo=None, id_=None, id_nome=None):
        super().__init__(numero, tipo)
        self.id = id_
        self.id_nome = id_nome


class DBTelefones(DBListaUnica):
    def __init__(self):
        super().__init__(DBTelefone)


class DBTiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)


class DBDadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, DBNome):
            raise TypeError("nome deve ser uma instância da classe DBNome")
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posicao = self.telefones.pesquisa(DBTelefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]
