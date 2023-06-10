from tkinter import *
from tkinter import messagebox

ventana = Tk()

def informacion():
    messagebox.showinfo("hola se corto correctamente")
def Advertencia():
    messagebox.showwarning("Alerta no se pude copiar ")
def error():
    messagebox.showerror("Error")

menubar = Menu(ventana)
ventana.config(menu=menubar)

#menu archivo

filemenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Nuevo")
filemenu.add_separator()
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir",command=ventana.quit)

editmenu=Menu(menubar)
menubar.add_cascade(label="Editar" , menu=editmenu)
editmenu.add_command(label="cortar",command=informacion)
editmenu.add_command(label="copiar" , command=Advertencia)
editmenu.add_command(label="pegar", command=error)

helpmenu=Menu(menubar)
menubar.add_cascade(label='ayuda')
helpmenu.add_command(label="Ayuda")



ventana.mainloop()