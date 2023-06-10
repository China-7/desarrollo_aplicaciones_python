from tkinter import*

V=Tk()


Menu_principal = Menu(V)


V.config(menu=Menu_principal, background="#169FFF")


#Archivo
Menu_Archivo = Menu(Menu_principal , tearoff=0)
Menu_principal.add_cascade(label="Archivo", menu =Menu_Archivo)
Menu_Archivo.add_command(label="Nuevo")
Menu_Archivo.add_separator()
Menu_Archivo.add_command(label="Abrir")
Menu_Archivo.add_command(label="Guardar")
Menu_Archivo.add_command(label="Cerrar")
Menu_Archivo.add_separator()
Menu_Archivo.add_command(label="Salir",command=V.quit)

Editar_Menu=Menu(Menu_principal)
Menu_principal.add_cascade(label="Edición" , menu=Editar_Menu)
Editar_Menu.add_command(label="cortar")
Editar_Menu.add_command(label="copiar" )
Editar_Menu.add_command(label="pegar")

Email_menu = Menu(Menu_principal)
Menu_principal.add_command(label="Email")


Imprimir_menu=Menu(Menu_principal)
Menu_principal.add_command(label="Imprimir")

#FRAMES
Frame_principal=Frame( background="#169FFF")
Frame_principal.grid(row=0 , column=0)
Frame_Radio_button=Frame(Frame_principal, background="#169FFF", width=50 , height=50)
Frame_Radio_button.grid(row=0, column=2)




#RADIO_BUTTON

Radio_Button = Radiobutton(Frame_Radio_button, text="Hoy" ,  background="#169FFF" )
Radio_Button.grid(row=0 , column=0)
Radio_Button = Radiobutton(Frame_Radio_button, text="Ayer",  background="#169FFF"  )
Radio_Button.grid(row=1 , column=0)
Radio_Button = Radiobutton(Frame_Radio_button, text="Esta Semana" ,  background="#169FFF" )
Radio_Button.grid(row=2 , column=0)
Radio_Button = Radiobutton(Frame_Radio_button, text="Este mes" ,  background="#169FFF" )
Radio_Button.grid(row=0 , column=1)
Radio_Button = Radiobutton(Frame_Radio_button, text="Mes Anterior" ,  background="#169FFF" )
Radio_Button.grid(row=1 , column=1)
Radio_Button = Radiobutton(Frame_Radio_button, text="Este Año" ,  background="#169FFF" )
Radio_Button.grid(row=2 , column=1)
Radio_Button = Radiobutton(Frame_Radio_button, text="Año Anterior"  ,  background="#169FFF")
Radio_Button.grid(row=2 , column=3)


#LABELS

Label_1 = Label(Frame_principal, text="Reportes de Facturacion", font=("Impact" , 35), fg="#0C0F9E",background="#169FFF")
Label_1.grid(row=0, column=0)






#ENTRYS


#BUTTONES



V.mainloop()