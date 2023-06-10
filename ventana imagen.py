from tkinter import *

V=Tk()
V.geometry("700x600+1+1")
V.title("cheilyn y lisania")
V.config(bg="#000")


imagenL=PhotoImage(file="jjjj.gif")
fondo=PhotoImage(file="jjjj.gif")
lblFondo=Label(V,image=fondo).place(x=100,y=100, width=("500") , height=("100"))
lblImagen=Label(V,image=imagenL).place(x=100,y=100)
V.mainloop()
