# 1 knop zorgt er voor dat het nummer in de label met 1 omhoog gaat
# 1 knop zorgt er voor dat het nummer in de label met 1 omlaag gaat.
# Als het nummer 0 is moet de achtergrond grijs zijn.
# Als het nummer kleiner dan 0 is moet de achtergrond rood zijn.
# Als het nummer groter dan 0 is moet de achtergrond groen zijn.
 

from tkinter import *
Window = Tk()
Window.title('Clicker')
Window.geometry('300x300')

Number = 0
Window.config(bg='grey')
def UPpressed():
    global Number
    Number += 1
    if Number == 0:
        Window.config(bg='grey')
    elif Number >0:
        Window.config(bg='green')
    else:
        Window.config(bg='red')
    Counter.config(text=f'{Number}')  #Counter['text'] = Number
    
def Downpressed():
    global Number
    Number -= 1
    if Number == 0:
        Window.config(bg='grey')
    elif Number >0:
        Window.config(bg='green')
    else:
        Window.config(bg='red') 
    Counter.config(text=f'{Number}')  

Up = Button(Window,
text='UP',
bg='green')
Up.pack(ipadx=10,ipady=30,fill='x')
Up.config(command=UPpressed)

Counter = Label(Window,
text=f'{Number}')
Counter.pack(anchor='center',ipadx=5,ipady=5,expand=True)

Down = Button(Window,
text='Down',
bg='red')
Down.pack(ipadx=10,ipady=30,fill='x',side='bottom')
Down.config(command=Downpressed)

Window.mainloop()