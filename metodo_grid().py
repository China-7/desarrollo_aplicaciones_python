from tkinter import*
ventana=Tk()
ventana.config(bg="#99F00C")
espacio01=Frame(ventana, width=200,height=200,bg="#2E8B57")
espacio01.pack()

labelNombre = Label(espacio01,text="Nombre: ",bg="#CCFF99")
labelNombre.grid(row=0, column=0, pady=10 , padx=15)

labelApe = Label(espacio01,text="Apellido: ",bg="#CAAEFF")
labelApe.grid(row=1, column=0,pady=10 , padx=15)

labelTel = Label(espacio01,text="Telefono: ",bg="#CCFF99")
labelTel.grid(row=2, column=0,  pady=10 , padx=15)

#=============Campos de Textos ===============

labelNombre = Entry(espacio01,bg="#CCFF99")
labelNombre.grid(row=0, column=1, pady=10 , padx=10)

labelApe = Entry(espacio01,bg="#CC00FF")
labelApe.grid(row=1, column=1,pady=10 , padx=15)

labelTel = Entry(espacio01,bg="#CCFF99")
labelTel.grid(row=2, column=1,  pady=10 , padx=15)


ventana.mainloop()
