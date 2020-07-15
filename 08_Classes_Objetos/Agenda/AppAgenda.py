from agenda import Agenda
from menu import Menu
from nome import Nome
from telefone import Telefone
from dado_agenda import DadoAgenda
import sys
import pickle
import os.path

class AppAgenda:
    @staticmethod
    def pede_nome():
        return input("Nome: ")

    @staticmethod
    def pede_telefone():
        return input("Telefone: ")

    @staticmethod
    def mostra_dados(dados):
        print(f"Nome: {dados.nome}")
        for telefone in dados.telefones:
            print(f"Telefone: {telefone}")
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        print(f"Nome: {dados.nome}")
        for i, telefone in enumerate(dados.telefones):
            print(f"{i} - Telefone: {telefone}")
        print()

    @staticmethod
    def pede_nome_arquivo():
        return input("Nome do arquivo: ")

    def __init__(self):
        self.agenda = Agenda()
        self.agenda.adicionaTipo("Celular")
        self.agenda.adicionaTipo("Residencia")
        self.agenda.adicionaTipo("Trabalho")
        self.agenda.adicionaTipo("Fax")
        self.menu = Menu()
        self.menu.adicionaopcao("Novo", self.novo)
        self.menu.adicionaopcao("Altera", self.altera)
        self.menu.adicionaopcao("Apaga", self.apaga)
        self.menu.adicionaopcao("Lista", self.lista)
        self.menu.adicionaopcao("Arquiva", self.arquiva)
        self.menu.adicionaopcao("Le arquivo", self.le)
        self.menu.adicionaopcao("Ordena", self.ordena)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrao=None):
        for i, tipo in enumerate(self.agenda.tiposTelefone):
            print(f" {i} - {tipo} ", end=None)
        t = Menu.valida_faixa_inteiro("Tipo: ", 0, len(self.agenda.tiposTelefone) - 1, padrao)
        return self.agenda.tiposTelefone[t]

    def pesquisa(self, nome):
        dado = self.agenda.pesquisaNome(nome)
        return dado

    # opção 1
    def novo(self):
        novo = AppAgenda.pede_nome()
        if Menu.nulo_ou_vazio(novo):
            return
        nome = Nome(novo)
        if self.pesquisa(nome) is not None:
            print("Nome ja existe!")
            return
        registro = DadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.adiciona(registro)

    # opção 2
    def altera(self):
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a alterar")
            return
        nome = AppAgenda.pede_nome()
        if Menu.nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            print("\nEncontrado:\n")
            AppAgenda.mostra_dados(p)
            print("Digite enter caso nao queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not Menu.nulo_ou_vazio(novo):
                p.nome = Nome(novo)
            self.menu_telefones(p)
        else:
            print("Nome não encontrado!")

    # opção 3
    def apaga(self):
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a apagar")
            return
        nome = AppAgenda.pede_nome()
        if Menu.nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            print(p)
            self.agenda.remove(p)
            print(f"Apagado. A agenda agora possui apenas: {len(self.agenda)} registros")
        else:
            print("Nome não encontrado.")

    # opção 4
    def lista(self):
        print("\nAgenda")
        print("-" * 60)
        for e in self.agenda:
            AppAgenda.mostra_dados(e)
        print("-" * 60)

    # opção 5
    def arquiva(self):
        if self.ultimo_nome is not None:
            print(f"Último nome utilizado foi '{self.ultimonome}'")
            print("Digite enter caso queira utilizar o mesmo nome")
        nome_arquivo = AppAgenda.pede_nome_arquivo()
        if Menu.nulo_ou_vazio(nome_arquivo):
            if self.ultimonome is not None:
                nome_arquivo = self.ultimonome
            else:
                return
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.agenda, arquivo)

    # opção 6
    def le(self, nome_arquivo=None):
        if nome_arquivo is None:
            nome_arquivo = AppAgenda.pede_nome_arquivo()
        if Menu.nulo_ou_vazio(nome_arquivo) or not os.path.isfile(nome_arquivo):
            return
        with open(nome_arquivo, "rb") as arquivo:
            self.agenda = pickle.load(arquivo)
        self.ultimo_nome = nome_arquivo

    # opção 7
    def ordena(self):
        self.agenda.ordena()
        print("\nAgenda ordenada\n")

    def menu_telefones(self, dados):
        while True:
            print("\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0:
                print("\n[A] - alterar\n[D] - apagar\n", end="")
            print("[N] - novo\n[S] - sair\n")
            operacao = input("Escolha uma operação: ")
            operacao = operacao.lower()
            if operacao not in ["a", "d", "n", "s"]:
                print("Operação inválida. Digite A, D, N ou S")
                continue
            if operacao == 'a' and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operacao == 'd' and len(dados.telefones) > 0:
                self.apaga_telefone(dados)
            elif operacao == 'n':
                self.novo_telefone(dados)
            elif operacao == "s":
                break

    # opção N
    def novo_telefone(self, dados):
        telefone = AppAgenda.pede_telefone()
        if Menu.nulo_ou_vazio(telefone):
            return
        if dados.pesquisaTelefone(telefone) is not None:
            print("Telefone ja existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(Telefone(telefone, tipo))

    # opção A
    def altera_telefones(self, dados):
        t = Menu.valida_faixa_inteiro_ou_branco("Digite a posição do "
                    "número a alterar, enter para sair: ", 0, len(dados.telefones) - 1)
        if t is Nome:
            return
        telefone = dados.telefones[t]
        print(f"Telefone: {telefone}")
        print("Digite enter caso não queira alterar o número")
        novotelefone = AppAgenda.pede_telefone()
        if not Menu.nulo_ou_vazio(novotelefone):
            telefone.nunero = novotelefone
        print("Digite enter caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(self.agenda.tiposTelefone.pesquisa(telefone.tipo))

    # opção D
    def apaga_telefone(self, dados):
        t = Menu.valida_faixa_inteiro_ou_branco("Digite a posição do "
                            "número a apagar, enter para sair: ", 0, len(dados.telefones) - 1)
        if t is None:
            return
        dados.telefones.remove(dados.telefones[t])

    def execute(self):
        self.menu.execute()

if __name__ == "__main__":
    app = AppAgenda()
    if len(sys.argv) > 1:
        app.le(sys.argv[1])
    app.execute()
