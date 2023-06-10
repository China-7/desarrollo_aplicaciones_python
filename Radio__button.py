from tkinter import *

Ventana = Tk()
Ventana.minsize(width = "300", height= "300")
Ventana.config(bg = "#9E256F")


def selecionado():
    Label1.config( text = opcion.get())
def reiniciar():
    opcion.set("none" )
    Label1.config(text="")

opcion = IntVar()

Radiobutton(Ventana , text = "Opcion 1" , variable = opcion , value = 1 , command = selecionado , width=100 , height=10).pack()
Radiobutton(Ventana , text = "Opcion 2" ,  variable = opcion , value = 2 , command = selecionado , width=100 , height=10).pack()
Radiobutton(Ventana , text = "Opcion 3" ,  variable = opcion , value = 3 , command = selecionado , width=100 , height=10).pack()

Label1 = Label(Ventana)
Label1.pack()

Button(Ventana, text = "Limpiar", command = reiniciar).pack()

Ventana.mainloop()