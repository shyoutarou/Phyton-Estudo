import numpy   as   np
import matplotlib.pyplot   as   plt

"""
pega primeiro digito n (1,2,3,4..) e P(n)
qtos tem eve porcentagem que aparece o digito
1200 dados no BD e compara pra ver se tem fraude
"""
plt.close("all")

prob_do_1o_grau = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9"]

porcentagens = [0.3010, 0.1761, 0.1249,
                0.0969, 0.0792, 0.0669,
                0.0580, 0.0512, 0.0458]

plt.bar(prob_do_1o_grau, porcentagens)

plt.xlabel("n")
plt.ylabel("P(n)")
plt.title("Estatística de Benford \n Para o Primeiro Dígito \n "
          "Estatística do Ladrão")

# List Conpreehensions dentro de função
# ValueError: too many values to unpack (expected 1)
# Pode colocar _(underline) como contador inves do i
# mas não é indicado
plt.xticks([nome for nome, i in enumerate(prob_do_1o_grau)], rotation="vertical")

plt.savefig("plot_bar_estatistica_benford.png")
plt.show()
