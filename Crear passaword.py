from tkinter import *

ventana = Tk()
ventana.config(bg="#C807CF")
ventana.geometry("500x500")
ventana.resizable(False , False)

miFrame = Frame(ventana, width = 200, height = 200 )
miFrame.pack()

#                                        Labes

labelUser = Label(miFrame , text = "Usuario:  ")
labelUser.grid(row = 0 , column = 0 , pady = 10, padx = 10)

labelPass = Label(miFrame , text = "Password:  ")
labelPass.grid(row = 1 , column = 0 , pady = 10, padx = 10)


#                                      ENTRYS


TextoUser = Entry(miFrame , justify = "center")
TextoUser.grid(row = 0 , column = 1)

TextoPass = Entry(miFrame , show = "-")
TextoPass.grid( row = 1 , column = 1 , pady = 10 , padx = 10)

BotonAceptar = Button (miFrame , text = "Aceptar" , command = exit)
BotonAceptar.grid(  row = 2 , column = 1 , pady = 10 , padx = 10 , columnspan = 2 )
BotonAceptar.config(width = 30)





ventana.mainloop()