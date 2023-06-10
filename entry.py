from tkinter import*
vL=Tk()
vL.geometry("700x500")

def mostrar():
      lab2=Label(jk, text=camp.get())
      lab2.place(x=20,y=70)
      
jk=Frame(vL, width="700",height="500")
jk.place(x=1,y=1)
jk.config(bg="yellow")

camp=Entry(jk)
camp.place(x=20, y=20)
camp.config(font=("cursive",20),bg="violet",fg="white")

boton=Button(jk, text="mostrar", command=mostrar)
boton.place(x=360, y=20)
boton.config(bg="black", fg="white", font=("arilla",15))
vL.mainloop()

