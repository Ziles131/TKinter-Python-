from tkinter import *
root = Tk()
root.title("backgroundcolor")
#root.geometry("450x222")
e1 = Entry(width=18, fg='black', justify = CENTER, font = '5')
lal = Label(width=15, height=1, fg='black', justify = CENTER, font = '8')
fr = Frame(root)
def insert1():
    e1.delete(0, END)
    e1.insert(0,"#ff0000")
    lal.config(text='красный', fg='#ff0000')
def insert2():
    e1.delete(0, END)
    e1.insert(0,"#ff7d00")
    lal.config(text='оранжевый', fg='#ff7d00')
def insert3():
    e1.delete(0, END)
    e1.insert(0,"#ffff00")
    lal.config(text='желтый', fg='#ffff00')
def insert4():
    e1.delete(0, END)
    e1.insert(0,"#00ff00")
    lal.config(text='зеленый', fg='#00ff00')
def insert5():
    e1.delete(0, END)
    e1.insert(0,"#007dff")
    lal.config(text='голубой', fg='#007dff')
def insert6():
    e1.delete(0, END)
    e1.insert(0,"#0000ff")
    lal.config(text='синий', fg='#0000ff')
def insert7():
    e1.delete(0, END)
    e1.insert(0,"#7d00ff")
    lal.config(text='фиолетовый', fg='#7d00ff')

b1 = Button(fr,bg='#ff0000', width=5, command = insert1)
b2 = Button(fr,bg='#ff7d00', width=5, command = insert2)
b3 = Button(fr,bg='#ffff00', width=5, command = insert3)
b4 = Button(fr,bg='#00ff00', width=5, command = insert4)
b5 = Button(fr,bg='#007dff', width=5, command = insert5)
b6 = Button(fr,bg='#0000ff', width=5, command = insert6)
b7 = Button(fr,bg='#7d00ff', width=5, command = insert7)

lal.pack(side = TOP, pady = 10)
e1.pack()
b1.pack(side = LEFT, padx = 5, pady = 8, ipady = 5)
b2.pack(side = LEFT, padx = 0, pady = 8, ipady = 5)
b3.pack(side = LEFT, padx = 5, pady = 8, ipady = 5)
b4.pack(side = LEFT, padx = 0, pady = 8, ipady = 5)
b5.pack(side = LEFT, padx = 5, pady = 8, ipady = 5)
b6.pack(side = LEFT, padx = 0, pady = 8, ipady = 5)
b7.pack(side = LEFT, padx = 5, pady = 8, ipady = 5)
fr.pack()
root.mainloop()
