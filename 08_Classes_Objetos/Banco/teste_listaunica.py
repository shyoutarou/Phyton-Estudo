from listaunica import *
lu = ListaUnica(int) 
lu.adiciona(5) 
lu.adiciona(3) 


print("Itens: " + str(len(lu)))

print(lu[1])

for e in lu:
    print(e)
