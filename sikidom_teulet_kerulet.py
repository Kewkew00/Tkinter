from tkinter import *
import math
#főablak
foablak = Tk()
foablak.title('Síkidom terület és kerület számítás')
foablak.minsize(width = 500, height = 100)
#főablak

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)


def haromszogterulet():

    def szamit():

        a = eval(mezo1.get())
        m = eval(mezo2.get())

        terulet = (a*m)/2

        mezo4.delete(0, END)
        mezo4.insert(0,str(terulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('háromszög terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'magasság(cm):')
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

def haromszogkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        kerulet = a+b+c

        if a <= 0 or b <= 0 or c <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(kerulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A téglatest területe')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
    szoveg3 = Label(ablak3, text = 'c(cm):')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    mezo4 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    ablak3.mainloop()


#file
def nevjegy():
    ablak2 = Toplevel(foablak)
    uzenet2 = Message(ablak2, text = 'Készítette:\n Csanádi Kevin \n Juhász Gábor \n Tarr Gábor', width = 300)
    gomb2 = Button(ablak2,text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()

menu2 = Menubutton(menusor, text = 'Fájl')
menu2.pack(side = LEFT)
fajl = Menu(menu2)
fajl.add_command(label ='Névjegy', command = nevjegy, )
fajl.add_command(label = 'Kilépés', command = foablak.destroy)
menu2.config(menu = fajl)
#file

#háromszög menü
menu1 = Menubutton(menusor, text = 'Háromszög')
menu1.pack(side = LEFT)
haromszog = Menu(menu1)
haromszog.add_command(label = 'Terület', command = haromszogterulet)
haromszog.add_command(label = 'Kerület', command = haromszogkerulet)
menu1.config(menu = haromszog)
#háromszög menü


foablak.mainloop()