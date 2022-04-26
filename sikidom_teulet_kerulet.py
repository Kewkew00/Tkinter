from tkinter import *
import math
#főablak
foablak = Tk()
foablak.title('Síkidom terület és kerület számítás')
foablak.minsize(width = 500, height = 100)
#főablak

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)


def haromszog():
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        m = eval(mezo2.get())
       
        terulet = a*m/2

    ablak3 =Toplevel(foablak)
    ablak3.title('háromszög terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a:')
    szoveg2 = Label(ablak3, text = 'magasság:')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo4 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    ablak3.mainloop()

#háromszög menü
menu1 = Menubutton(menusor, text = 'Háromszög')
menu1.pack(side = LEFT)
haromszog = Menu(menu1)
haromszog.add_command(label = 'Terület', command = haromszog)
#teglatest.add_command(label = 'Térfogat', command = terfogat)
menu1.config(menu = haromszog)
#háromszög menü

foablak.mainloop()