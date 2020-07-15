from tkinter import *

Relevos = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE]

Bitmaps = ['error', 'gray75', 'gray50', 'gray25', 'gray12',
           'hourglass', 'info', 'questhead', 'question', 'warning']

window = Tk()

window.title('BITMAPS e RELEVOS Python')

row = 0
col = 0
for bit in Relevos:
    e = Button(window, text=bit, relief=bit, font=(None, 10))
    e.grid(row=row, column=col, sticky=E + W)
    row += 1

for rel in Bitmaps:
    if (row > 4):
        row = 0
        col += 1

    e = Button(window, text=rel, bitmap=rel, relief=RAISED, font=(None, 10))
    e.grid(row=row, column=col, sticky=E + W)
    row += 1

window.geometry("300x200+10+20")
window.mainloop()
