import tkinter as tk

V=tk.Tk()
V.title("Mi aplicacion")
V.minsize(width=800 , height=300)

A=tk.Frame()
A.place(width="500" , height="500")
A.config(bg="lightgreen" , relief="groove", bd=20)

A.pack()
#_-_-_-_-_-_Funciones_-_-_-_-_-_

def cuenta_numeros(): 
      contador=int(numero["text"])
      contador += 1
      numero.config(text=contador)

def Restar_numeros():
     restando=int(numero["text"])
     restando -=1
     numero.config(text=restando)

#####  Label Titulo #####
titulo=tk.Label(A,
                text="Contador",
                font=("Arial", 24),
                bg="lightgreen", fg="darkgreen",
                relief=tk.GROOVE,
                padx=20, pady=20)
titulo.pack()


########## Label numero ##########
numero=tk.Label(A,
                text=0,
                font=("Arial", 48),
                bg="darkgreen",
                fg="lightgreen",
                padx=20, pady=20)
                             
numero.pack()

########## BONTON CONTAR ##########

añadir=tk.Button(A,
                 text="Contar",
                 font=("Arial", 18),
                 bg="lightgreen",
                 fg="black",
                 padx=20 , pady=20,
                 relief="groove", bd=8,
                 command=cuenta_numeros)


añadir.pack()

#Boton restar


restar=tk.Button(A,
                 text="restar",
                 bg="lightgreen",
                 command=Restar_numeros,
                 width="20", height="5",
                 relief="groove", bd=5)


      

restar.pack()
     

V.mainloop()
