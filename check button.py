from tkinter import *

ventana = Tk()


def seleccionar():
    cadena += "Marcador 01"

    if (marcar01.get()):
          cadena += "Marcador 01"
    else:
         cadena += "Desmarcado 02"


    if (marcar02.get()):
          cadena += "Marcador 01"

    else:
         cadena += "Desmarcar 02"

    mostrar.config(text = cadena)

marcar01 = IntVar()
marcar02 = IntVar()


Checkbutton (ventana , text="Marcar 01" , onvalue=1, offvalue=0 , variable=marcar01 , command=seleccionar).pack()
Checkbutton (ventana , text="Marcar 02" , onvalue=1, offvalue=0 , variable=marcar02 , command=seleccionar).pack()

mostrar = Label(ventana)
mostrar.pack()

ventana.mainloop()