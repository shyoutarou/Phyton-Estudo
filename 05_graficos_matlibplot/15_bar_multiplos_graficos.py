import numpy   as   np
import matplotlib.pyplot   as   plt

# Gráfigo de Comparação entre resultados te´pricos e experimentais...

plt.close("all")

rotulos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
y_um = [0.30, 0.18, 0.12, 0.10, 0.08, 0.07, 0.06, 0.05, 0.05]
y_dois = [0.28, 0.19, 0.19, 0.08, 0.07, 0.06, 0.06, 0.06, 0.00]

# x = Local dos rótulos
x = np.arange(len(rotulos))
# Largura = Largura das barras
largura = 0.35

#Colocar [] para ficar implicito que é list, funcao de multiplo retornos
[figura, subgraficos] = plt.subplots()
rect1 = subgraficos.bar(x - largura / 2, y_um, largura, label='Teorico')
rect2 = subgraficos.bar(x + largura / 2, y_dois, largura, label='Experimental')

# Adiconar os rótulos, título e personalizar p eixo x da base dos rótulos, etc..
subgraficos.set_ylabel('Porcentagem')
subgraficos.set_title('Porcentagem por ' + "Operador")
subgraficos.set_xticks(x)
subgraficos.set_xticklabels(rotulos)
subgraficos.legend()

def autolabel(rects):
    # Anexar um rótulo de texto acima de cada barraem rects para exibir sua altura
    for rect in rects:
        height = rect.get_height()
        subgraficos.annotate('{}'.format(height),
                             xy=(rect.get_x() + rect.get_width() / 2, height),
                             xytext=(0, 3), # 0 em x , 3 em y
                             textcoords="offset points",
                             ha='center', va='bottom')

autolabel(rect1)
autolabel(rect2)

figura.tight_layout()

# dpi densidade de pontos por inch,
plt.savefig("plot_bar_multiplos_graficos.png", dpi=100)
plt.show()
