from tkinter import *

ventana = Tk()
ventana.config(bg = "#000000")

miFrame = Frame(ventana)
miFrame.pack()

campoTexto = Text(miFrame)
campoTexto.grid(row = 0 , column =0)
campoTexto.config( width = 40 , height = 20)
campoTexto.config(bg = "#000", fg = "#1DFF31" , fon = ("Arial", 20), relief = "sunken", bd =20)

scrollvert = Scrollbar(miFrame , command = campoTexto.yview)
scrollvert.grid(row = 0 , column = 1 , sticky = "nesw") 
campoTexto.config(yscrollcommand = scrollvert.set)

ventana.mainloop()