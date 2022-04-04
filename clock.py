
from tkinter import *
# * = hoeft je niet meer tk.Label te doen etc en lan je gewoon rooot = Tk()
 
#strftime importeert de tijd van de systeem
from time import strftime
 

root = Tk()
root.title('Clock')
 

def time():
    Time = strftime('%H:%M:%S')
    lbl.config(text = Time) #lbl is een afkorting voor label
    lbl.after(1000, time)
 

lbl = Label(root, font = ('Label Bigness', 100, 'bold'),
            background = 'red',
            foreground = 'dark blue')

 

lbl.pack(anchor= 'center') # is positie van de label in de window
time()
 
mainloop()