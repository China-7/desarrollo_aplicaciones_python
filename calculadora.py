from tkinter import Button,Tk,Frame,Entry,END

ventana=Tk()
ventana.geometry('800x700')
ventana.config(bg="#FFFFFF")
ventana.resizable(0,0)
ventana.title("calculadora")

class HoverButton(Button):
      def __init__(self,master,**kw):
            Button.__init__(self, master=master,**kw)
            self.defaultBackground=self["background"]
            self.bind('<Enter>', self.on_enter)
            self.bind('<Leave>', self.on_leave)

      def on_enter(self, e):
            self['background']=['activebackground']
      def on_leave(self, e):
            self['background']= self.defaultBackground

i=0
def obtener(dato):
      global i
      i+=1
      Resultado.insert(i, dato)

def operacion():
      global i
      ecuacion=Resultado.get()
      if i !=0:
            try:
                  result=str(eval (ecuacion))
                  Resultado.delete(0,END)
                  Resultado.insert(0,result)
                  longitud = len(result)
                  i=longitud
            except:
                  result = 'ERROR'
                  Resultado.delete(0,END)
                  Resultado.insert
      else:
            pass
def borrar_uno():
      global i
      if i==-1:
            pass
      else:
            Resultado.delete(i, last=None)
def borrar_todo():
      Resultado.delete(0,END)
      

frame=Frame(ventana, bg="#000000", relief = 'raised')
frame.grid(column = 0 , row = 0, padx=6, pady=3)

Resultado = Entry(frame, bg='#9EF8E8', width=18, relief = 'groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan = 4 , row = 0, pady = 3, padx = 1,ipadx = 1 , ipady = 1)

#Fila 1

Button1 = HoverButton(frame , text = '1' , borderwidth = 2, height = 2 , width = 5 , font = ('Comic sens MC', 12,'bold'),
                       relief = 'raised' , activebackground = 'aqua', bg = '#999AB8' , anchor = "center" ,
                       command = lambda: obtener(1))
Button1.grid(column = 0 , row = 1 , pady = 1 , padx = 3)

Button2 = HoverButton(frame , text = '2' , borderwidth = 2, height = 2 , width = 5 , font = ('Comic sens MC', 12,'bold'),
                       relief = 'raised' , activebackground = 'yellow', bg = '#909AB8' , anchor = "center" ,
                       command = lambda: obtener(2))
Button2.grid(column = 1 , row = 1 , pady = 1 , padx = 1)

Button3 = HoverButton ( frame , text = 3 , borderwidth = 2, height = 2 , width = 5 , font = ('Comic sens MC', 12,'bold'),
                       relief = 'raised' , activebackground = 'yellow', bg = '#909AB8' , anchor = "center" , command = lambda: obtener(3 )
  )                  
Button3.grid(column = 2 , row = 1 , pady = 1 , padx = 1)


ventana.mainloop()


      
