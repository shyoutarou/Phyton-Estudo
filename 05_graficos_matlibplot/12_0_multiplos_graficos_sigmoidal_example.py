import numpy   as   np
import matplotlib.pylab as plt
import matplotlib.ticker as ticker

plt.close("all")

sigmoid = lambda x: 1 / (1 + np.exp(-x))

x = plt.linspace(-10,10,10)
y =  plt.linspace(-10,10,100)

f = sigmoid(x)
g = sigmoid(y)

plt.plot(x, f,'r', label='linspace(-10,10,10)')
plt.plot(y, g,'b', label='linspace(-10,10,100)')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Função Sigmoidal")
plt.suptitle('Sigmoid')
plt.text(4,0.8,r'$\sigma(x)=\frac{1}{1+e^{-x}}$',fontsize=15)
plt.grid()
plt.legend(loc='lower right')

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.1))

plt.legend(bbox_to_anchor=(0.5, -0.2), loc='center', borderaxespad=0)

plt.subplots_adjust(bottom=0.22)

plt.savefig("plot_multiplos_graficos_sigmoidal_example.png")
plt.show()


