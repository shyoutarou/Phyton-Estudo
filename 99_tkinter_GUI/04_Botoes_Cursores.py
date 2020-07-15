from tkinter import *

CURSORES = ['arrow', 'exchange', 'pirate', 'spraycan', 'watch', 'circle',
            'fleur', 'plus', 'star', 'clock', 'heart', 'shuttle',
            'target', 'cross', 'man', 'sizing', 'tcross', 'dotbox',
            'mouse', 'spider', 'trek']

window = Tk()

window.title('CURSORES Python')

row = 0
col = 0
for cursor in CURSORES:
    e = Button(window, text=cursor, cursor=cursor,
               font=(None, 10))
    e.grid(row=row, column=col, sticky=E + W)
    row += 1
    if (row > 4):
        row = 0
        col += 1

window.geometry("300x200+10+20")
window.mainloop()
