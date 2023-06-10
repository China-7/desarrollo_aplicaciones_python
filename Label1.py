from tkinter import*
V=Tk()
V.geometry("630x360")
miFrame=Frame()
miFrame.place(x=120 , y=100)
#miFrame.pack(side="right")
miFrame.config(width="300", height="200")
miFrame.config(bg="blue" ,bd=20)
miFrame.config(relief="groove",cursor="pirate")

V.mainloop()
