pdv_loja_tres = 39, 31, 39, "Lider", 39, 37, 39, 31
print(type(pdv_loja_tres))

print(pdv_loja_tres[5])

pdv_loja_quatro = [31, 39, 37, 31, 36, 37, 31, 31,
                   "Supervisor", 36, 36, 31, 39, 31]
print(type(pdv_loja_quatro))

tds_os_pdvs = pdv_loja_tres, pdv_loja_quatro
print(tds_os_pdvs)

#Tuple com multiplos objetos
tupla_multipla = ([1,2,3], [3,2,1])
print(tupla_multipla)

#Alterar dados
# tds_os_pdvs[1] = 99
# TypeError: 'tuple' object does not support item assignment

