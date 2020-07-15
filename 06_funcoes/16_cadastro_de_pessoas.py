#	Perceber que, as listas globais, sempre devem estar fora das
#	funções para que todas as funções possam acessa-las.

#	Lista para receber cada CPF
CPFs =  []
#	Lista para receber cada nome
nomes = []
#	Lista para receber cada celular
celulares = []

#	Esta função e a ultima a ser criada
def main_cadastro_de_pessoas():
    resposta = bool(int(input("Deseja cadastrar CPF? Digitar 1 (um) "
                              "para sim e 0 (zero) para não.")))

    while resposta == True:
        cadastrar_CPF()
        # Ou seja, depois de cadatrar o	CPF, a aplicagao
        # pergunta se deseja fazer uma consulta
        consultar()
        resposta = bool(int(input("Deseja cadastrar CPF? Digitar 1 (um) "
                                  "para sim e 0 (zero) para não.")))


#	Esta e a primeira function a ser	desenvoivida
def cadastrar_CPF():
    # Esta e a primeira function a ser desenvolvida
    def cadastrar_CPF():
        global CPFs, cpf, nomes, nome, celulares, celular
        # NAO confundir a variavel	no	singu	lar com	a variavel	no	plural

        cpf = input("Digitar o numero do CPF: ")
        while cpf in CPFs:
            print("0 CPF digitado ja existe!")
            cpf = int(input("Digitar o numero do CPF: "))
        CPFs.append(cpf)

        nome = input("Digitar o nome: ")
        while nome in nomes:
            print("0 nome digitado ja existe!")
            nome = input("Digitar o nome: ")
        nomes.append(nome)

        celular = input("Digitar o numero de celular: ")
        while celular in celulares:
            print("0 numero de celular digitado ja existe!")
            celular = input("Digitar o numero de celular: ")
        celulares.append(celular)

# Esta e a segunda function a ser desenvolvida
def consultar():
    global cpf, nome, celular
    resposta = bool(int(input("Deseja consultar CPF? Digitar 1 (um)"
                              " para sim e 0 (zero) para não.")))
    if resposta == True:
        print("0 nome do CPF", cpf, "e:", nome)
        print("0 numero do celular do CPF", cpf, "e:", celular)

#	Perceber que, e necessario chamar uma fungao principal, normalmente
#	a chamada de "main" para que o codigo desenvolvido
#	poder ser executado
main_cadastro_de_pessoas()

#	EXERCICIO: Fazer um cadastro de produtos (Para Casa).