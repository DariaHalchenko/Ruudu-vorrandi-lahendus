from tkinter import *
from tkinter import messagebox as mb 
import matplotlib.pyplot as plt 
import numpy as np  
global graf
import math

def lahendus(): 
    try:
        a = float(a_.get()) 
        b = float(b_.get()) 
        c = float(c_.get()) 
    except:
        mb.showwarning("Tähelepanu!","On vaja sisestada numbrid!")
        return
    diskrimineerija=b**2-4*a*c
    if diskrimineerija > 0:
        x1 = round((-1*b+math.sqrt(diskrimineerija))/(2*a),2)
        x2 = round((-1*b-math.sqrt(diskrimineerija))/(2*a),2)
        t = f'D = {diskrimineerija}\nx₁ = {x1}\nx₂ = {x2}'
        graf=True
    elif diskrimineerija == 0:
        x=round((-1*b)/(2*a),2)
        t = f'D = {diskrimineerija}\nx = {x}'
        graf=True
    else:
        t="Нет корней"
        graf=False
    tulemus.delete(1.0, END)
    tulemus.insert(END, t, "center")
    

def graafik():
    a = float(a_.get()) 
    b = float(b_.get()) 
    c = float(c_.get()) 
    disc=b**2-4*a*c
    if disc<0:
        mb.showwarning("Tähelepanu!","Ei ole võimalus graafikut luua!")
        return
    x0=(-b)/(2*a)
    y0=a*x0**2+b*x0+c
    x1= np.arange(x0-10, x0+10, 0.5)#min max step [min,max]
    y1=a*x1**2+b*x1+c
    plt.figure()
    plt.plot(x1, y1,'c-.o')
    plt.title("Квадратное уравнение")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def kala():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,'b:*',x2,y2,'b:*',x3,y3,'b:*',x4,y4,'b:*',x5,y5,'b:*',x6,y6,'b:*',x7,y7,'b:*',x8,y8, 'b:*',x9,y9, 'b:*', x10,y10,'k-')
    plt.title("Кит")
    plt.xlabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def vihmavari ():
    x1=np.arange(-12, 12, 0.5)
    y1=-(1/18)*x1**2+12
    x2=np.arange(-4, 4, 0.5) 
    y2=-(1/8)*x2**2+6
    x3=np.arange(-12, -4, 0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4, 12, 0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,'r-.d',x2,y2,'r-.d',x3,y3,'r-.d',x4,y4,'r-.d',x5,y5,'m-s',x6,y6, 'm-s')
    plt.title("Зонтик")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show() 


def prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = -(1/16) * (x1 + 5)**2 + 2
    x2 = np.arange(1, 9.5, 0.5)
    y2 = -(1/16) * (x2 - 5)**2 + 2
    x3 = np.arange(-9, -0.5, 0.5)
    y3 = (1/4) * (x3 + 5)**2 - 3
    x4 = np.arange(1, 9.5, 0.5)
    y4 = (1/4) * (x4 - 5)**2 - 3
    x5 = np.arange(-9, -6, 0.5)
    y5 = -(x5 + 7)**2 + 5
    x6 = np.arange(6, 9.5, 0.5)
    y6 = -(x6 - 7)**2 + 5
    x7 = np.arange(-1, 1, 0.01)
    y7 = -0.5 * (x7**2) + 1.5
    plt.figure()
    plt.plot(x1,y1, 'k-+',x2,y2,'k-+',x3,y3,'k-+',x4,y4,'k-+',x5,y5,'k-+',x6,y6,'k-+',x7,y7,'k-+')
    plt.title("Очки")
    plt.xlabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()



aken=Tk() 
aken.geometry("1500x600") 
aken.iconbitmap('puzzle.ico') 
aken.title("Решение квадратного уравнения")
tekst="Решение квадратного уравнения\n"
pealkiri=Label(aken,
               text=tekst,
               bg="#00ff00",
               fg="#080808",
               font="Algerian 35",
               height=3,
               width=len(tekst), 
               cursor="watch") 
a_ = Entry(aken, 
          bg="#00ffff",
          fg="#080808",
          font="Algerian 30",
          width=15,
          justify=CENTER)
b_ = Entry(aken, 
          bg="#00ffff",
          fg="#080808",
          font="Algerian 30",
          width=15,
          justify=CENTER)
c_ = Entry(aken,
           bg="#00ffff",
           fg="#080808",
           font="Algerian 30",
           width=15,
           justify=CENTER) 


ka_la = Radiobutton(aken, 
                    text="Кит", 
                    font=("Algerian", 40), 
                    value=1, 
                    command=kala)
vihma_vari= Radiobutton(aken, 
                        text="Зонтик", 
                        font=("Algerian ", 40), 
                        value=2, 
                        command=vihmavari )
pri_llid = Radiobutton(aken, 
                       text="Очки", 
                       font=("Algerian ", 40), 
                       value=3, 
                       command=prillid) 

text_1 = Label(aken, text="x**2 +", font=("Times New Roman", 30))
text_2 = Label(aken, text="x +", font=("Times New Roman", 30)) 
text_3 = Label(aken, text="=0", font=("Times New Roman", 30))  

lahendus_button = Button(aken, text="Решить", font=("Algerian", 30), command=lahendus)
pealkiri.grid(row=0, column=0, columnspan=7)
graafik_button = Button(aken, text="График", font=("Algerian", 30), command=graafik)  
tulemus = Text (aken, height=5, width=15, font=("Wide Latin", 15)) 
tulemus.grid(row=4, column=2, columnspan=4) 

lahendus_button.grid(row=3, rowspan=1, column=1, columnspan=2)
graafik_button.grid(row=3, rowspan=1, column=3, columnspan=2)
a_.grid(row=1, column=1)
text_1.grid(row=1, column=2)
b_.grid(row=1, column=3)
text_2.grid(row=1, column=4)
c_.grid(row=1, column=5)
text_3.grid(row=1, column=6) 

ka_la.grid(row=5, column=1, columnspan=3)
vihma_vari.grid(row=5, column=2, columnspan=3)
pri_llid.grid(row=5, column=3, columnspan=3)

for i in range(7):
    aken.grid_columnconfigure(i, weight=1)

for i in range(6):
    aken.grid_rowconfigure(i, weight=1)

aken.mainloop() 
