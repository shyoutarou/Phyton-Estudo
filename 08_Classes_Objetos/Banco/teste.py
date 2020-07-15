from clientes import Cliente
from bancos import Banco
from contas import Conta, ContaEspecial

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
jose = Cliente("Jose Vargas", "9721-3040")

print(joao.nome)

cc_joao = Conta(joao, 1, 100)
cc_maria = Conta(maria, 2)

conta_esp = ContaEspecial([maria, joao], 2, 500, 1000) 

tatu = Banco("Banco TATU")

tatu.abre_conta(cc_joao)
tatu.abre_conta(cc_maria)
tatu.lista_contas()

##cc_joao.resumo()
##cc_joao.deposito(50)
##cc_joao.resumo()
##cc_joao.saque(100)
##cc_joao.resumo()

cc_joao.extrato()

cc_maria.deposito(50)
cc_maria.extrato()

conta_esp = ContaEspecial([maria, joao], 3, 500, 1000) 
conta_esp.deposito(300)
conta_esp.deposito(95.15)
conta_esp.saque(1500)
conta_esp.extrato()
