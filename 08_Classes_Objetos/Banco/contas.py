class Conta:
    def __init__(self, clientes, numero, saldo=0):

        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = [] 
        self.deposito(saldo) 

    def resumo(self):
        print(f"CC Numero: {self.numero} Saldo: {self.saldo}") 
    def saque(self, valor):
        if self.saldo >= valor: 
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor]) 
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])
    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        print(f"Saldo Anterior: {self.saldo:10.2f}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}") 
        print(f"\n      Saldo: {self.saldo:10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo) 
        self.limite = limite 
    def saque(self, valor):
        if self.saldo + self.limite >= valor: 
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        
        



