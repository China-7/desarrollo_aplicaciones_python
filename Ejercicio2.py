#Formulario de regitro con sqlite i python -tkinter codigo completo eigtha

from tkinter import messagebox

#python image library

from PIL import ImageTk,Image
 
import sqlite3

class resgistro:
      db_name='database_proyecto.db'
      
      def __init__(self,ventana):
            self.window=ventana
            self.window.title("Formulario de registro")
            self.window.geometry("390x540")
            self.window.resizable(0,0)
            self.window.config(bd=10)


#=============Titulo=======================

titulo=Label(ventana, text="Registro de Usuario" , fg="black",font=("comic Sans", 13, "bold"),pady=10)



imagen_calculadora=Image.open('hola.png')
nueva_imagen=imagen_calculadora.resize((40,40))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen.image=render
label_imagen.pack(pady=5)

#          marco

marco=labelFrame(ventana, text="Datos personales",font=("Comic Sans",10,"bold"))
marco.config(bd=2)
marco.pack()




#------------------------------------------Formulario----------------------------------------

label_dni=Label(marco, text='DNI', font=("Comic Sans",10 ,'bold')).grid(row=0,column=0,sticky='s')
self.dni=Entry(marco,width=25)
self.dni.grid(row=0, column=1,padx=5,pady=10)

label_Nombre=Label(marco, text='Nombre', font=("Comic Sans",10 ,'bold')).grid(row=1,column=0,sticky='s')
self.Nombre=Entry(marco,width=25)
self.Nombre.grid(row=1, column=1,padx=5,pady=10)

label_Apellidos=Label(marco, text='Apellidos', font=("Comic Sans",10 ,'bold')).grid(row=2,column=0,sticky='s')
self.Apellidos=Entry(marco,width=25)
self.Apellidos.grid(row=2, column=1,padx=5,pady=10)

label_Sexo=Label(marco, text='Sexo', font=("Comic Sans",10 ,'bold')).grid(row=3,column=0,sticky='s')
self.combo_sexo=tkk.combobox(marco,values=['masculino','Femenino'], width=22)
self.Sexo.grid(row=3, column=1,padx=5,pady=10)

label_Edad=Label(marco, text='Edad', font=("Comic Sans",10 ,'bold')).grid(row=4,column=0,sticky='s')
self.Edad=Entry(marco,width=25)
self.Edad.grid(row=4, column=1,padx=5,pady=10)

label_Correo=Label(marco, text='Correo Electronico  :', font=("Comic Sans",10 ,'bold')).grid(row=5 ,column=0,sticky='s')
self.Correo=Entry(marco,width=25)
self.Correo.grid(row=5, column=1,padx=5,pady=10)

label_passaword=Label(marco, text='Contraseña :', font=("Comic Sans",10 ,'bold')).grid(row=6 ,column=0,sticky='s')
self.passaword=Entry(marco,width=25, show='*')
self.passaword.grid(row=6, column=1,padx=5,pady=10)


label_passaword=Label(marco, text='Contraseña :', font=("Comic Sans",10 ,'bold')).grid(row=7 ,column=0,sticky='s')
self.repetir=Entry(marco,width=25,show='*')
self.repetir.grid(row=7, column=1,padx=5,pady=10)


"--------------Frame botones-------------"

frame_botones=Frame(ventana)
frame_botones.pack()

boton_registrar=Button(frame_botones, text='Registrar', command=self.)














ventana.mainloop()







