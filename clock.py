
from tkinter import *
# * = hoeft je niet meer tk.Label te doen etc en lan je gewoon root = Tk()
 
#strftime importeert de tijd van de systeem
from time import strftime
 

root = Tk()
root.title('Clock')
 

def time():
    Time = strftime('%H:%M:%S')
    lbl.config(text = Time) #lbl is een afkorting voor label
    lbl.after(1000,time)


lbl = Label(root, font = ('Label Bigness', 100, 'bold'),
            background = 'pink',
            foreground = 'blue') #active background is de kleur wanneer je het aan klikt. expand is wanneer je de label meer ruimte geeft om zich heen.

 

lbl.pack(anchor= 'center') # is positie van de label in de window
time()
 
mainloop()