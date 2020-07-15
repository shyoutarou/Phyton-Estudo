import tkinter as tk
from tkinter import font
from tkinter import messagebox

import sys


class myApp(object):

    def __init__(self, **kw):
        # insira toda a inicialização aqui

        self.root = tk.Tk()
        self.root.title("Mostra Fonts")
        self.root.geometry('400x600')
        self.create_menu_bar()
        self.create_canvas_area()
        self.create_status_bar()

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # codigo para apresentação dos fonts disponiveis no sistema
        fonts = list(font.families())
        fonts.sort()

        pagTexto = tk.Text(self.root, height=50, width=50, yscrollcommand=scrollbar.set)
        pagTexto.pack()
        scrollbar.config(command=pagTexto.yview)

        posicaoFont = 0

        for item in fonts:
            strPos = str(posicaoFont)
            posicaoFont = posicaoFont + 1

            pagTexto.tag_config(strPos, font=(item, 14))
            pagTexto.insert(tk.END, item, strPos)
            pagTexto.insert(tk.END, "\n")

    def create_status_bar(self):
        self.status = tk.Label(self.root,
                               text="Bem vindo ao visualizador de fonts do caderno de laboratório",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks()

    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.finaliza_software)

        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

    def create_canvas_area(self):
        pass

    def finaliza_software(self):
        self.root.quit()

    def mnu_about(self):
        msg = "Este programa mostra os fonts existentes no sistema \n "
        msg += "Mais informações visite www.cadernodelaboratorio.com.br"

        messagebox.showinfo("Sobre mostraFonts v 0.1", msg)

    def execute(self):
        self.root.mainloop()


def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))