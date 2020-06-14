from tkinter import *
 
def but1():
    a = lbox1.curselection()
    for i in a:
        lbox2.insert(END, lbox1.get(i))
        lbox1.delete(i)
def but2():
    a = lbox2.curselection()
    for i in a:
        lbox1.insert(END, lbox2.get(i))
        lbox2.delete(i)
root = Tk()

 
lbox1 = Listbox(selectmode=EXTENDED)
a = "12345"
for i in a:
    lbox1.insert(END, i)
lbox1.pack(side=LEFT)
lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=RIGHT)
scroll = Scrollbar(command=lbox1.yview)
scroll.pack(side=LEFT, fill=Y)
lbox1.config(yscrollcommand=scroll.set)
 
f = Frame()
f.pack(side=LEFT, padx=10)
button1 = Button(f, text = '>>>', command = but1)
button1.pack()
button2 = Button(f, text = '<<<', command = but2)
button2.pack()
 
root.mainloop()





