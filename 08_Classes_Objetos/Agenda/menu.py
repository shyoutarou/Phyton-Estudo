class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adicionaopcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i}] - {opcao[0]}")
            print()

    @staticmethod
    def nulo_ou_vazio(texto):
        return texto is None or not texto.strip()

    @staticmethod
    def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
        while True:
            try:
                entrada = input(pergunta)
                if Menu.nulo_ou_vazio(entrada):
                    return None
                valor = int(entrada)
                if inicio <= valor <= fim:
                    return valor
            except ValueError:
                print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

    @staticmethod
    def valida_faixa_inteiro(pergunta, inicio, fim, padrao=None):
        while True:
            try:
                entrada = input(pergunta)
                if Menu.nulo_ou_vazio(entrada) and padrao is not None:
                    entrada = padrao
                valor = int(entrada)
                if inicio <= valor <= fim:
                    return valor
            except ValueError:
                print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

    def execute(self):
        while True:
            self.exibe()
            escolha = Menu.valida_faixa_inteiro("Escolha uma opção: ",
                                                0, len(self.opcoes) - 1)
            if escolha == 0:
                break
            self.opcoes[escolha][1]()
