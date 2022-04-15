from tkinter import *
Window = Tk()
Window.title('Hello')
Window.geometry('100x100')
Window.config(bg='dark blue')
box1 = Label(Window,bg='dark blue').pack(ipadx=5,ipady=5,fill='y')
box2 = Label(Window,text='Hello Tkinter!',bg='red',fg='yellow').pack(ipadx=10,ipady=10,fill='x')

Window.mainloop()
