from tkinter import*

V=Tk()
V.geometry("1000x490")
V.title("Frame")

FRAME=Frame(width="1000", height="400",bg="#AC44FF")
FRAME.place(x=20 , y=20)

#Campo de texto

texto01=Entry(FRAME)
texto01.config(bg="#CDFF51", fg="#B72BFF")
texto01.icursor(0) 
texto01.insert(0,"JAJAJA")
texto01.pack() 
#texto01.delete(0,END)


def imprimir():
      label01=Label(FRAME,text=("=> "+texto01.get()))
      label01.pack()
      label01.config(bg='#000000', fg="#0CF508",fon=('consolas',14))
      
boton=Button(FRAME, text="imprimir", command=imprimir)
boton.pack()
V.mainloop()

#,isinstance(texto01.get(),str)
