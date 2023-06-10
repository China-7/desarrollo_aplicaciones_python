from tkinter import *
ventana=Tk()
ventana.geometry("1200x600")
def saludar():
      labe=Label(frame, text="Hola mundo")
      labe.place(x=60 , y=20)
      labe.config(padx="200",pady="40", bg="#FF0000", fon="arial, 20")

      
def Hambre():
      label=Label(frame,text="tengo hambre", padx="40" , pady="30", bg="yellow")
      label.place(x=280, y=300)
      



frame=Frame(ventana ,width="1500" ,height="800")
frame.pack() 
#frame.place(x=2, y=5)
frame.config(bg="purple")
boton1=Button(frame , text="Saludar", command=saludar)
boton1.place(x=100 , y=200)

imsaludar=PhotoImage(file="hola.png")
boton2=Button(frame, image=imsaludar , command=saludar)
boton2.place(x=580 , y=200)


boton3=Button(frame, text="presiona", command=Hambre)
boton3.place(x=200, y=200)

ventana.mainloop()


