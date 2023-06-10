from tkinter import ttk
from tkinter import *

import sqlite3
class Productos:
      def __init__(self , root):
            self.wind=root
            self.wind.title("Productos")
            self.wind.geometry("200x200")
            self.wind.config(bg="dark blue")

            frame1=LabelFrame(self.wind, text="Informacion" , font=("Currier",20) , bg="black" , fg="red")
            frame2=LabelFrame(self.wind, text="Hola" , font=("Currier", 20) ,bg="black" , fg="red")
            frame3=LabelFrame(self.wind, text="Datos del producto" , font=("Currier", 20) ,bg="black" , fg="red")
            frame1.pack(fill="both" , expand="yes",padx=30, pady=10)
            frame2.pack(fill="both", expand="yes" , padx=30, pady=10)
            frame3.pack(fill="both" , expand="yes",padx=30, pady=10)
           
            
if __name__=='__main__':
      root=Tk()
      product=Productos(root)
      root.mainloop()
