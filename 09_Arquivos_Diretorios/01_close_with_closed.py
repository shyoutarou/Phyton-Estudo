"""
# FileNotFoundError: [Errno 2] No such file or directory: 'nome-errado.text'
f = open('nome-errado.text', 'r')
"""

arquivo = open('nome_errado.txt', 'r')
conteudo_arquivo = arquivo.read()

print('Arquivo fechado? {}'.format(arquivo.closed))
if not arquivo.closed:
    arquivo.close()
    print("Arquivo fechado? {}".format(arquivo.closed))

"""
for line in open("myfile.txt"):
    print(line, end="")
    
O problema com esse código é que ele deixa o arquivo aberto 
por um período indeterminado após a execução da parte do código. 
Isso não é um problema em scripts simples, mas pode ser um 
problema para aplicativos maiores. A instrução with permite 
que objetos como arquivos sejam usados de uma maneira que 
garanta que eles sempre sejam limpos de forma rápida e correta.  
Devemos sempre fechar o arquivo aberto.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

"""
arquivo.close()

"""
with open('/some/file', 'rb') as f:
    parser = ParserClasss(f)
    return list(parser.info())

"""
