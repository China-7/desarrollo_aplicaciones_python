from tkinter import *
from tkinter import messagebox

ventana = Tk()



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
editmenu.add_command(label="cortar")
editmenu.add_command(label="copiar" )
editmenu.add_command(label="pegar")

helpmenu=Menu(menubar)
menubar.add_cascade(label='ayuda', menu=helpmenu)
helpmenu.add_command(label="Ayuda")



ventana.mainloop()