"""
ID ESTUDIANTE
NOMBRE
TELEFONO
CORREO ELECTRONICO
DIRECCION
"""
from tkinter import *

V=Tk()
V.minsize(width="700", height="500")

def mostrar():
      lab1=Label(text=ID1.get())
      lab1.place(x=100,y=270)
def mostrar2():
       lab2=Label(text=nom1.get())
       lab2.place(x=100 , y=270)
def mostrar3():
       lab3=Label(text=tel1.get())
       lab3.place(x=100 , y=270)


ID=Label(text="ID ESTUDIANTE", width="80" , height="5" ,  bg="yellow")
ID.place(x=1, y=20)
ID1=Entry(ID)
ID1.place(x=360,y=28)

nom=Label(text="Nombre" , width="80", height="5",bg="#ED31F7")
nom.place(x=1, y=100)
nom1=Entry(nom)
nom1.place(x=360,y=28)

tel=Label(text="Telefono",width="80",height="5",bg="#13F789" )
tel.place(x=1 ,y=180)
tel1=Entry(tel)
tel1.place(x=370,y=28)

img=PhotoImage(file="hola.png")
boton2=Button(image=img , command=mostrar)
boton2.place(x=1000 , y=290)


