from tkinter import *
import math
#főablak
foablak = Tk()
foablak.title('Síkidom terület és kerület számítás')
foablak.minsize(width = 600, height = 100)
#főablak

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)


def haromszogterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        m = eval(mezo2.get())

        terulet = (a*m)/2

        if a <= 0 or m <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terulet))

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

    #Háromszög rajz
    c = Canvas(ablak3, width=120, height=125, bg="white")
    c.create_polygon(65, 35, 45, 110, 80, 110, outline = "black", width=4 , fill = "white")
    c.grid(row=1, column=4, rowspan=7)    
    #Háromszög rajz

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
    ablak3.title('A háromszög területe')
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

    #Háromszög rajz
    c = Canvas(ablak3, width=120, height=125, bg="white")
    c.create_polygon(65, 35, 45, 110, 80, 110, outline = "black", width=4 , fill = "white")
    c.grid(row=1, column=4, rowspan=7)    
    #Háromszög rajz

    ablak3.mainloop()

def trapezterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        c = eval(mezo2.get())
        m = eval(mezo3.get())
        terulet = (a+c)*m/2

        if a <= 0 or m <= 0 or c <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A trapéz területe')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'c(cm):')
    szoveg3 = Label(ablak3, text = 'magasság(cm):')
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

    trapez = Canvas(ablak3, width = 190, height = 150, bg = "white")
    trapez.create_line(15, 125, 185, 125, fill="black", width = 1)
    trapez.create_line(140, 50, 60, 50, fill = "black", width = 1)
    trapez.create_line(15, 125, 60, 50, fill = "black")
    trapez.create_line(185, 125, 140, 50, fill = "black")
    trapez.create_line(100, 125, 100, 50, fill = "black", width = 1)
    trapez.grid(column = 3, row = 1, rowspan = 8)

    ablak3.mainloop()

def trapezkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        d = eval(mezo5.get())
        kerulet = a+b+c+d

        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            mezo4.delete(0, END)
            mezo4.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(kerulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A trapéz területe')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
    szoveg3 = Label(ablak3, text = 'c(cm):')
    szoveg5 = Label(ablak3, text = 'd(cm):')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    mezo5 = Entry(ablak3)
    mezo4 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg5.grid(row = 4)
    szoveg4.grid(row = 6)
    gomb1.grid(row = 5, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo5.grid(row = 4, column = 2, sticky = W)
    mezo4.grid(row = 6, column = 2, sticky = W)

    trapez = Canvas(ablak3, width = 190, height = 150, bg = "white")
    trapez.create_line(15, 125, 185, 125, fill="black", width = 1)
    trapez.create_line(140, 50, 60, 50, fill = "black", width = 1)
    trapez.create_line(15, 125, 60, 50, fill = "black")
    trapez.create_line(185, 125, 140, 50, fill = "black")
    trapez.create_line(100, 125, 100, 50, fill = "black", width = 1)
    trapez.grid(column = 3, row = 1, rowspan = 8)

    ablak3.mainloop()

def rombuszterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo3.delete(0, END)
            mezo3.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        m = eval(mezo2.get())
        terulet = a*m

        if a <= 0 or m <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo3.delete(0, END)
            mezo3.insert(0, str(terulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A rombusz területe')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'magasság(cm):')
    szoveg3 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 4)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    gomb1.grid(row = 3, column = 2, sticky = W)
    mezo3.grid(row = 4, column = 2, sticky = W)
    ablak3.mainloop()

def rombuszkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo3.delete(0, END)
            mezo3.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        terulet = 4*a

        if a <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo3.delete(0, END)
            mezo3.insert(0, str(terulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A rombusz kerülete')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg3 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg3.grid(row = 4)
    mezo1.grid(row = 1, column = 2, sticky = W)
    gomb1.grid(row = 3, column = 2, sticky = W)
    mezo3.grid(row = 4, column = 2, sticky = W)
    ablak3.mainloop()

def negyzetterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo3.delete(0, END)
            mezo3.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        terulet = a*a

        if a <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo3.delete(0, END)
            mezo3.insert(0, str(terulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A négyzet területe')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg3 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg3.grid(row = 4)
    mezo1.grid(row = 1, column = 2, sticky = W)
    gomb1.grid(row = 3, column = 2, sticky = W)
    mezo3.grid(row = 4, column = 2, sticky = W)
    ablak3.mainloop()

def negyzetkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo3.delete(0, END)
            mezo3.insert(0, str()+ 'A számításhoz számadat kell')

        a = eval(mezo1.get())
        terulet = 4*a

        if a <= 0:
            mezo3.delete(0, END)
            mezo3.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo3.delete(0, END)
            mezo3.insert(0, str(terulet))

    ablak3 =Toplevel(foablak)
    ablak3.title('A négyzet kerülete')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg3 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg3.grid(row = 4)
    mezo1.grid(row = 1, column = 2, sticky = W)
    gomb1.grid(row = 3, column = 2, sticky = W)
    mezo3.grid(row = 4, column = 2, sticky = W)
    ablak3.mainloop()

def paralelogrammaterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        m = eval(mezo2.get())

        terulet = a*m

        mezo4.delete(0, END)
        mezo4.insert(0,str(terulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Paralelogramma terület számítás')
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

    c = Canvas(ablak3, width=150, height=150, bg="white")
    c.create_polygon(65, 55, 37.5, 110, 110, 110, 135, 55, outline = "black", fill = "white")
    c.create_line(65, 55, 37.5, 110, fill='black',)
    c.create_line(65, 55, 135, 55, fill='black',)    
    c.grid(row=1, column=4, rowspan=7)

    ablak3.mainloop()

def paralelogrammakerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        b = eval(mezo2.get())

        kerulet = 2*(a+b)

        mezo4.delete(0, END)
        mezo4.insert(0,str(kerulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Paralelogramma terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
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

    c = Canvas(ablak3, width=150, height=150, bg="white")
    c.create_polygon(65, 55, 37.5, 110, 110, 110, 135, 55, outline = "black", fill = "white")
    c.create_line(65, 55, 37.5, 110, fill='black',)
    c.create_line(65, 55, 135, 55, fill='black',)    
    c.grid(row=1, column=4, rowspan=7)

    ablak3.mainloop()

def teglalapterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        b = eval(mezo2.get())

        terulet = a*b

        mezo4.delete(0, END)
        mezo4.insert(0,str(terulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Téglalap terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
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

def teglalapkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        b = eval(mezo2.get())

        kerulet = 2*(a+b)

        mezo4.delete(0, END)
        mezo4.insert(0,str(kerulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Téglalap terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
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

def deltoidterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        a = eval(mezo1.get())
        b = eval(mezo2.get())

        terulet = 2*(a+b)

        mezo4.delete(0, END)
        mezo4.insert(0,str(terulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Deltoid terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a(cm):')
    szoveg2 = Label(ablak3, text = 'b(cm):')
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

    c = Canvas(ablak3, width=110, height=110)
    c.create_polygon(25,42.5,62.5,5,100,40,62.5,87.5, fill="white", outline = 'black')
    c.create_line(25,42.5,62.5,5, fill="black",)
    c.grid(row = 2, column = 4, rowspan=7,)

    ablak3.mainloop()

def deltoidkerulet():

    s = ''

    def szamit():

        if not s:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+ 'A számításhoz számadat kell')


        e = eval(mezo1.get())
        f = eval(mezo2.get())

        kerulet = (e*f)/2

        mezo4.delete(0, END)
        mezo4.insert(0,str(kerulet))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Deltoid terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'e(cm):')
    szoveg2 = Label(ablak3, text = 'f(cm):')
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

    c = Canvas(ablak3, width=110, height=110)
    c.create_polygon(25,42.5,62.5,5,100,40,62.5,87.5, fill="white", outline = 'black')
    c.create_line(25,42.5,62.5,5, fill="black",)
    c.grid(row = 2, column = 4, rowspan=7,)

    ablak3.mainloop()

def korterulet():
    
    s = ''

    def szamit():

        if not s:
            mezo2.delete(0, END)
            mezo2.insert(0, str()+ 'A számításhoz számadat kell')
        
        r = eval(mezo1.get())

        terulet = math.pi*(r*r)

        if r <= 0:
            mezo2.delete(0, END)
            mezo2.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo2.delete(0, END)
            mezo2.insert(0, str(round(terulet)))

    ablak3 =Toplevel(foablak)
    ablak3.title('Kör terület számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'r(cm):')
    szoveg2 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 3)
    gomb1.grid(row = 2, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 3, column = 2, sticky = W)

    #Kör rajz
    c = Canvas(ablak3, width=120, height=120, bg="white")
    c.create_oval(30,30,105,105, fill='black')
    c.grid(row=1, column=4, rowspan=7)
    #Kör rajz

    ablak3.mainloop()

def korkerulet():
    
    s = ''

    def szamit():

        if not s:
            mezo2.delete(0, END)
            mezo2.insert(0, str()+ 'A számításhoz számadat kell')


        r = eval(mezo1.get())

        terulet = 2*math.pi*r

        if r <= 0:
            mezo2.delete(0, END)
            mezo2.insert(0,str()+ 'Negatív számmal nem lehet számolni')
        else:
            mezo2.delete(0, END)
            mezo2.insert(0, str(round(terulet)))

        mezo2.delete(0, END)
        mezo2.insert(0,str(round(terulet)))
       
    ablak3 =Toplevel(foablak)
    ablak3.title('Kör kerülek számítás')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'r(cm):')
    szoveg2 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 3)
    gomb1.grid(row = 2, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 3, column = 2, sticky = W)

    #Kör rajz
    c = Canvas(ablak3, width=120, height=120, bg="white")
    c.create_oval(30,30,105,105, fill='black')
    c.grid(row=1, column=4, rowspan=7)
    #Kör rajz

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

#trapéz menü
menu3 = Menubutton(menusor, text = 'Trapéz')
menu3.pack(side = LEFT)
trapez = Menu(menu3)
trapez.add_command(label = 'Terület', command = trapezterulet)
trapez.add_command(label = 'Kerület', command = trapezkerulet)
menu3.config(menu = trapez)
#trapéz menü

#rombusz menü
menu4 = Menubutton(menusor, text = 'Rombusz')
menu4.pack(side = LEFT)
rombusz = Menu(menu4)
rombusz.add_command(label = 'Terület', command = rombuszterulet)
rombusz.add_command(label = 'Kerület', command = rombuszkerulet)
menu4.config(menu = rombusz)
#rombusz menü

#négyzet menü
menu5 = Menubutton(menusor, text = 'Négyzet')
menu5.pack(side = LEFT)
negyzet = Menu(menu5)
negyzet.add_command(label = 'Terület', command = negyzetterulet)
negyzet.add_command(label = 'Kerület', command = negyzetkerulet)
menu5.config(menu = negyzet)
#négyzet menü

#paralelogramma menü
menu6 = Menubutton(menusor, text = 'Paralelogramma')
menu6.pack(side = LEFT)
paralelogramma = Menu(menu6)
paralelogramma.add_command(label = 'Terület', command = paralelogrammaterulet)
paralelogramma.add_command(label = 'Kerület', command = paralelogrammakerulet)
menu6.config(menu = paralelogramma)
#paralelogramma menü

#téglalap menü
menu7 = Menubutton(menusor, text = 'Téglalap')
menu7.pack(side = LEFT)
teglalap = Menu(menu7)
teglalap.add_command(label = 'Terület', command = teglalapterulet)
teglalap.add_command(label = 'Kerület', command = teglalapkerulet)
menu7.config(menu = teglalap)
#téglalap menü

#deltoid menü
menu8 = Menubutton(menusor, text = 'Deltoid')
menu8.pack(side = LEFT)
deltoid = Menu(menu8)
deltoid.add_command(label = 'Terület', command = deltoidterulet)
deltoid.add_command(label = 'Kerület', command = deltoidkerulet)
menu8.config(menu = deltoid)
#deltoid menü

#kor menü
menu8 = Menubutton(menusor, text = 'Kör')
menu8.pack(side = LEFT)
kor = Menu(menu8)
kor.add_command(label = 'Terület', command = korterulet)
kor.add_command(label = 'Kerület', command = korkerulet)
menu8.config(menu = kor)
#kor menü

foablak.mainloop()