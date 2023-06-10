from tkinter import *
from tkinter import messagebox

ventana = Tk()

def informacion():
    messagebox.showinfo("hola se corto correctamente")
def Advertencia():
    messagebox.showwarning("Alerta no se pude copiar ")
def error():
    messagebox.showerror("Error")


def pregunta():
    """
   # valor = messagebox.askquestion("Salir","¿Estas seguro de salir?")

   
    if valor == "yes":
        ventana.quit()

"""

    valor = messagebox.askyesno("Salir","¿Estas seguro de salir?")
    if valor:
        ventana.quit()
def Aceptar():
    ventana.destroy()

def reintentar():
    valor = messagebox.askretrycancel("Reintentar", "Ocurrio un error")
    pass


menubar = Menu(ventana)
ventana.config(menu=menubar)

#menu archivo

filemenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Nuevo", command=reintentar)
filemenu.add_separator()
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar", command=Aceptar)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=pregunta)

editmenu=Menu(menubar)
menubar.add_cascade(label="Editar" , menu=editmenu)
editmenu.add_command(label="cortar",command=informacion)
editmenu.add_command(label="copiar" , command=Advertencia)
editmenu.add_command(label="pegar", command=error)

helpmenu=Menu(menubar)
menubar.add_cascade(label='ayuda')
helpmenu.add_command(label="Ayuda")



ventana.mainloop()