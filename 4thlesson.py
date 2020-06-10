'''from tkinter import *
root = Tk()
l1 = Label(bg="lightgreen", width=30, height=10, text="This is a label", font="Arial 32")
l1.pack(expand=1, fill=BOTH)
root.mainloop()
'''
from tkinter import *
root = Tk()
#root.geometry('480x240')
d = {
    'Ира': 'Лидникова',
    'Маша': 'Серпученко',
    'Иван': 'Масляников'
}
fr = Frame(root, bg = 'silver')
fr2 = Frame(root)
def change():
    if var.get() == 0:
        l['text'] = d['Ира']
    elif var.get() == 1:
        l['text'] = d['Маша']
    elif var.get() == 2:
        l['text'] = d['Иван']
l = Label(fr2, text = 'Фамилия', bg = 'silver', fg = 'yellow', font = 'Arial 14')
var = IntVar()
var.set(0)
c1 = Radiobutton(fr, indicatoron=0, command = change, width = 15, height = 3,
                 text = 'Ира', bg = 'lightgreen', variable = var, value = 0)
c2 = Radiobutton(fr, indicatoron=0, command = change, width = 15, height = 3,
                 text = 'Маша', bg = 'lightgreen', variable = var, value = 1)
c3 = Radiobutton(fr, indicatoron=0, command = change, width = 15, height = 3,
                 text = 'Иван', bg = 'lightgreen', variable = var, value = 2)
fr.pack(expand = 0, side = LEFT, anchor = W)
fr2.pack(expand = 0, side = LEFT, anchor = W)
l.pack(side = TOP, ipady = 70.5, ipadx = 45)
c1.pack(side = TOP, pady = 1, anchor = W)
c2.pack(side = TOP, anchor = W)
c3.pack(side = TOP, pady = 1, anchor = W)


root.mainloop()






