import tkinter as tk
Window = tk.Tk()
Window.title('Hello')
Window.geometry('100x100')
Window.config(bg='dark blue')
box1 = tk.Label(Window,text='Hello Tkinter!',bg='red',fg='yellow').pack(ipadx=10,ipady=10)
Window.mainloop()
