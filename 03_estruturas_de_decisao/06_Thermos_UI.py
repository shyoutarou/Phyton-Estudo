from tkinter import *


def resultado():
    frase = entradaTemperatura.get()
    frase = frase.upper()
    if ("C") in frase:
        c = frase.strip('C')
        kelvin = 273.15 + int(c)
        fraseKelvin = "Kelvin:" + str(kelvin)
        fahr = (9 * int(c) + 160) / 5
        #fahr = (int(c) * 9 / 5) + 32
        fraseFahr = "Fahrenheit:" + str(fahr)
        labelTemperatura1.config(text=fraseKelvin)
        labelTemperatura2.config(text=fraseFahr)
    elif ("K") in frase:
        k = frase.strip('K')
        celsius = int(k) - 273.15
        fraseCelsius = "Celsius:" + str(celsius)
        fahr = (9 * (int(k) - 273.15) + 160) / 5
        # fahr = ((int(k) - 273,15) * 9 / 5) + 32
        fraseFahr = "Fahrenheit:" + str(fahr)
        labelTemperatura1.config(text=fraseCelsius)
        labelTemperatura2.config(text=fraseFahr)
    elif ("F") in frase:
        f = frase.strip('F')
        celsius = (int(f) - 32) * 5 / 9
        fraseCelsius = "Celsius:" + str(celsius)
        kelvin = (int(f) - 32) * 5 / 9 + 273.15
        fraseKelvin = "Kelvin:" + str(kelvin)
        labelTemperatura1.config(text=fraseCelsius)
        labelTemperatura2.config(text=fraseKelvin)
    pass


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
labelTemperatura = Label(frame1, text="Temperatura:")
labelTemperatura1 = Label(frame2)
labelTemperatura1.pack(side=LEFT)
labelTemperatura2 = Label(frame2)
labelTemperatura2.pack(side=LEFT)
entradaTemperatura = Entry(frame1, width=20)
botaoCalcular = Button(frame1, text="Calcular", command=resultado)
labelTemperatura.pack(side=LEFT, pady=20)
entradaTemperatura.pack(side=LEFT)
botaoCalcular.pack(side=LEFT)
frame1.pack(side=TOP)
frame2.pack(side=TOP)
root.resizable(width=False, height=False)
root.title("Conversor de Temperatura.")
root.geometry("300x100")
root.mainloop()
