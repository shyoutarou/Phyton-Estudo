from tkinter import *


def categoria(imc):
    categorias = ["Abaixo do Peso", "Peso Normal(Saudável)",
                  "Acima do peso(Sobrepeso)", "Obesidade Grau I(Gordo)",
                  "Obesidade Grau II(Severa)", "Obesidade Grau III(Mórbido)"]
    if (imc <= 18.5):
        return categorias[0]
    elif (imc > 18.5 and imc < 24.9):
        return categorias[1]
    elif (imc > 24.9 and imc < 29.9):
        return categorias[2]
    elif (imc > 29.9 and imc < 34.9):
        return categorias[3]
    elif (imc > 34.9 and imc < 39.9):
        return categorias[4]
    else:
        return categorias[5]

class MyWindow:
    def __init__(self, win):

        self.lblmassa = Label(win, text='Digitar sua massa: ')
        self.lblaltura = Label(win, text='Digitar sua altura: ')
        self.lblimc = Label(win, text='IMC: ')
        self.lblpesoideal = Label(win, text='Peso ideal: ')
        self.lblcategoria = Label(win, text='')
        self.lblmsg = Label(window, text="")
        self.lblmsg.place(x=80, y=145)

        self.lblmassa.place(x=70, y=70)
        self.lblaltura.place(x=70, y=120)
        self.lblimc.place(x=70, y=220)
        self.lblpesoideal.place(x=180, y=220)
        self.lblcategoria.place(x=70, y=250)

        self.massa = Entry(bd=3,width=15)
        self.altura = Entry(bd=3,width=15)

        self.massa.place(x=180, y=70)
        self.altura.place(x=180, y=120)

        self.b1 = Button(win, text='Calcular', command=self.peso)
        self.b1.place(x=150, y=170)

    def peso(self):
        self.lblimc.config(text="IMC: ")
        self.lblpesoideal.config(text="Peso Ideal: ")
        self.lblcategoria.config(text="")
        lblmsg = Label(window, text="")
        lblmsg.place(x=80, y=145)

        try:
            massa = float(self.massa.get())
        except ValueError:
            self.lblmsg.config(text="Digitar somente números na massa!", pady=5, fg="red")
            return

        try:
            altura = float(self.altura.get())
        except ValueError:
            self.lblmsg.config(text="Digitar somente números na altura!", pady=5, fg="red")
            return

        imc = massa / altura ** 2
        result = '{:.2f}'.format(imc)
        self.lblmsg.config(text="")

        if (v0.get() == 1):
            peso_ideal = (72.2 * altura) - 57
        else:
            peso_ideal = (62.1 * altura) - 44.7

        self.lblimc.config(text="IMC: " + str(result))
        self.lblpesoideal.config(text="Peso Ideal: {:.2f}".format(peso_ideal))
        self.lblcategoria.config(text="Categoria: " + categoria(imc))

window = Tk()
window.resizable(width=False,height=False)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="Masculino", variable=v0, value=1)
r2 = Radiobutton(window, text="Feminino", variable=v0, value=2)
r1.place(x=80, y=25)
r2.place(x=200, y=25)

mywin = MyWindow(window)
window.title('Cálculo IMC')
window.geometry("400x280+10+10")
window.mainloop()
