def clear():#ункция очистки окна
    list = root.grid_slaves()
    for l in list:
        l.destroy()
import matplotlib.pyplot as plt
import numpy as np

import os
def hist():#остроение диаграммы
    global n
    n = 0

    def tabl():#Создание таблицы данных
        def expand():#Расширение таблицы
            global n
            n += 1
            a.append(Label(text=str(n+1)))
            b.append(Entry())
            a[n].grid(row=4 + n, column=1, sticky="w")
            b[n].grid(row=4 + n, column=2, sticky="w")
            btn2.grid(row=4 + n + 1)
            btn3.grid(row=4 + n + 1)

        def delete():#Укорачивание таблицы
            global n
            if n != 0:
                a[n].destroy()
                b[n].destroy()
                del (a[n])
                del (b[n])
                n -= 1
                btn2.grid(row=4 + n + 1)
                btn3.grid(row=4 + n + 1)

        def postroi():#Построение самого графика
            x = []
            y = []
            for i in range(len(a)):
                x.append(np.double(b[i].get()))

            x = np.asarray(x)
            y = np.asarray(y)
            xlabel = name_entry.get()
            ylabel = surname_entry.get()
            xlabel = 'r"' + xlabel
            ylabel = 'r"' + ylabel
            xlabel = xlabel + '"'
            ylabel = ylabel + '"'
            n, bins, patches = plt.hist(x, x.size, density=True, facecolor='red')
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            plt.show()

        a = [Label(text=str(n+1))]
        b = [Entry()]

        a[0].grid(row=4, column=1, sticky="w")
        b[0].grid(row=4, column=2, sticky="w")
        btn2 = Button(text="Добавить строку", command=expand)
        btn2.grid(column=1)
        btn3 = Button(text="Удалить строку", command=delete)
        btn3.grid(column=2, row=5)
        btn4 = Button(text="Посторить график", command=postroi)
        btn4.grid(row=4 + n)

    clear()

    def nametabl():#Создание названия таблицы

        name_label1 = Label(text=name_entry.get()).grid(row=3, column=1, sticky="w")
        surname_label1 = Label(text=surname_entry.get()).grid(row=3, column=2, sticky="w")
        tabl()

    name_label = Label(text="Ось x")
    surname_label = Label(text="Ось y ")

    name_label.grid(row=0, column=0, sticky="w")
    surname_label.grid(row=1, column=0, sticky="w")

    name_entry = Entry()
    surname_entry = Entry()

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    surname_entry.grid(row=1, column=1, padx=5, pady=5)
    btn = Button(text="Применить названия к осям", command=nametabl)
    btn.grid(row=3 + n)
def Graphe():#Построение графика
    global n
    n = 0


    def tabl():#Аналогично с гистограммой
        def expand():
            global n
            n+=1
            a.append(Entry())
            b.append(Entry())
            a[n].grid(row=4+n, column=2, sticky="w")
            b[n].grid(row=4+n, column=3, sticky="w")
            btn2.grid(row=4 + n+1)
            btn3.grid(row=4+n+1)
        def delete():
            global n
            if n!=0:
             a[n].destroy()
             b[n].destroy()
             del(a[n])
             del(b[n])
             n -= 1
             btn2.grid(row=4 + n+1,column=2)
             btn3.grid(row=4+n+1, column=3)
        def postroi():
            global name3
            try:
                os.remove("graph.jpg")
            except OSError as e:  ## if failed, report it back to the user ##
                print()
            x=[]
            y=[]
            for i in range(len(a)):
                x.append(np.double(a[i].get()))
                y.append(np.double(b[i].get()))
            x = np.asarray(x)
            y = np.asarray(y)
            xlabel = name_entry.get()
            ylabel = surname_entry.get()
            xlabel = 'r"' + xlabel
            ylabel = 'r"' + ylabel
            xlabel = xlabel + '"'
            ylabel = ylabel + '"'
            p, v = np.polyfit(x, y, deg=int(name3.get()), cov=True)
            p_f = np.poly1d(p)
            c=str()
            for i in range(len(p)):
                c+="x^"+str(i)+"*"+str("%.3f" %(p[i]))+"+"

            lbl = Label(text="y="+c)
            lbl.grid(row=0, column=3)

            x1 = np.arange(x.min(), x.max(), 0.0001)
            fig, ax = plt.subplots()
            ax.plot(x1, p_f(x1), color='blue', linewidth=1)
            ax.plot(x, y, 'ro')
            ax.minorticks_on()
            ax.grid(which='major',
                    color='k',
                    linewidth=2)
            ax.grid(which='minor',
                    color='k',
                    linestyle=':')
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            fig.set_figwidth(12)
            fig.set_figheight(6)
            plt.savefig("graph.jpg")
            plt.show()

        def logar():#Логарифмирование оси икс

            global name3
            x=[]
            y=[]
            for i in range(len(a)):
                x.append(np.log(np.double(a[i].get())))
                y.append(np.log(np.double(b[i].get())))
            x= np.asarray(x)
            y = np.asarray(y)
            xlabel = name_entry.get()
            ylabel = surname_entry.get()
            xlabel = 'r"lg(' + xlabel
            ylabel = 'r"' + ylabel
            xlabel = xlabel + ')"'
            ylabel = ylabel + '"'
            p, v = np.polyfit(x, y, deg=int(name3.get()), cov=True)
            p_f = np.poly1d(p)
            c=str()
            for i in range(len(p)):
                c+="x^"+str(i)+"*"+str("%.3f" %(p[i]))

            lbl = Label(text=c)
            lbl.grid(row=0, column=3)

            x1 = np.arange(x.min(), x.max(), 0.0001)
            fig, ax = plt.subplots()
            ax.plot(x1, p_f(x1), color='blue', linewidth=1)
            ax.plot(x, y, 'ro')
            ax.minorticks_on()
            ax.grid(which='major',
                    color='k',
                    linewidth=2)
            ax.grid(which='minor',
                    color='k',
                    linestyle=':')
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            fig.set_figwidth(12)
            fig.set_figheight(6)
            plt.savefig("graph.jpg")
            plt.show()




        a=[Entry()]
        b=[Entry()]

        a[0].grid(row=4, column=2, sticky="w")
        b[0].grid(row=4, column=3, sticky="w")
        btn2 = Button(text="Добавить строку", command=expand)
        btn2.grid(column=2)
        btn3=Button(text="Удалить строку", command=delete)
        btn3.grid(column=3,row=5)
        name_label2 = Label(text="Степень уравнения апроксимации").grid(row=4, column=0, sticky="w")
        global name3
        name3=Entry()
        name3.grid(row=4, column=1, sticky="w")
        btn4=Button(text="Посторить график", command=postroi)
        btn4.grid(row=5+n)
        btn5 = Button(text="Логарифмировать ось икс", command=logar)
        btn5.grid(row=6 + n)

    clear()
    def nametabl():

        name_label1 = Label(text=name_entry.get()).grid(row=3, column=2, sticky="w")
        surname_label1 = Label(text=surname_entry.get()).grid(row=3, column=3, sticky="w")
        tabl()

    name_label = Label(text="Ось x")
    surname_label = Label(text="Ось y ")

    name_label.grid(row=0, column=0, sticky="w")
    surname_label.grid(row=1, column=0, sticky="w")

    name_entry = Entry()
    surname_entry = Entry()

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    surname_entry.grid(row=1, column=1, padx=5, pady=5)
    btn = Button(text="Применить названия к осям",command=nametabl)
    btn.grid(row=3+n)

from tkinter import *
root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Апроксимировать График", command=Graphe)
helpmenu.add_command(label="Создать Гистограмму", command=hist)
mainmenu.add_cascade(label="Функции",
                     menu=helpmenu)

root.mainloop()