from tkinter import*

#Creacion de la configuracion de la ventana

V = Tk()
V.title("Reajuste de producto terminado")
V.geometry("900x700")
#V.config(bg="#24B00D")

# Frames


frame = Frame(V)
frame.grid(row = 0 , column = 0)

frame_2 = Frame(V)
frame_2.place(x = 1 , y = 190)
frame_3 = Frame(V,width=200)
frame_3.place(x=1 , y =250)
frame_4 = Frame(V, bg="#B208E5", width=800, height=500)
frame_4.place(x=1 , y = 310)
frame_5 = Frame(V, bg="#E51466", width=800, height=500, relief="solid",bd=2)
frame_5.place(x=700 , y = 310)

#botones

Salir = Button(frame, width = 20 , height = 10, bg = "#C431FF" ,text = "Salir")
Salir.grid(row = 0 , column =0)

Grabar = Button(frame, width = 20 , height = 10, bg = "#C431FF" , text = "Grabar")
Grabar.grid(row = 0 , column = 1)

Buscar = Button(frame, width = 20 , height = 10, bg = "#C431FF", text = "Buscar")
Buscar.grid(row = 0 , column =2)

Imprimir = Button(frame, width = 20 , height = 10, bg = "#C431FF" , text = "Imprimir")
Imprimir.grid(row = 0 , column = 3)

Ayuda = Button(frame, width = 20 , height = 10, bg = "#C431FF" , text = "Ayuda")
Ayuda.grid(row = 0 , column = 4)

#labes

Label1 = Label(frame_2 , text = "Almacen :" , font=("Lemon", 15))
Label1.grid(row=0 , column=0)
Label2  = Label(frame_2 , text = "Codigo :" , font=("Lemon", 15))
Label2.grid(row=1 , column=0)
Label3  = Label(frame_2 , text = "Ref :" , font=("Lemon", 15))
Label3.grid(row=1 , column=2)
Label4  = Label(frame_2 , text = " Ref No :" , font=("Lemon", 15))
Label4.grid(row=1 , column=4)
Label_en_blanco = Label(frame_3 , text = "                    " , font=("Lemon", 15))
Label_en_blanco.grid(row=0 , column=2)
Label5  = Label(frame_3 , text = " Fecha :" , font=("Lemon", 15))
Label5.grid(row=1 , column=4)
Label6  = Label(frame_4 , text = " Fecha :" , font=("Lemon", 15))
Label6.grid(row=1 , column=4)


#Entry

Entry_1 = Entry(frame_2 , relief= "solid" , bd = "5", width=50)
Entry_1.grid(row=0, column=1 )
Entry_2 = Entry(frame_2 , relief= "solid" , bd = "5", width=50)
Entry_2.grid(row=1, column=1 )
Entry_3 = Entry(frame_2 , relief= "solid" , bd = "5", width=80)
Entry_3.grid(row=1, column=3 )
Entry_4 = Entry(frame_2 , relief= "solid" , bd = "5", width=45)
Entry_4.grid(row=1, column=6  )

Entry_5 = Entry(frame_3,relief= "solid" , bd = "5", width=140)
Entry_5.grid(row=1, column=3)




V.mainloop()





