# Maak een programmatje dat:

# Een GUI opend met een knop er in waarop grabbelen staat
# Een label met het aantal items in de grabbelton
# Als je op de knop drukt moet je het bericht te zien krijgen: “Gefeliciteerd, je hebt een {item} gegrabbeld!”
# Op de plek van {item} in de tekst moet een woord komen die je random uit een lijst met minimaal 10 verschillende woorden haalt
# Daarna moet het aantal items worden aangepast en mag dat woord niet meer terug komen.
from msilib.schema import RadioButton
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from turtle import position
import random

Window = Tk()
Window.config(bg = 'blue')
Window.geometry('250x250')

Itemlijst = ['Appel','Peer','Banaan','Perziek','Advocado','Mango','Sinasappel','Manderijn','Kiwi','Cocosnoot']

def gekozen():
        RandomItem = random.choice(Itemlijst)
        Gekozenitem['text'] =f'U heeft {RandomItem} gewonnen!'
        Itemlijst.remove(RandomItem)
def aantalitemtext():
        Aantal['text'] = f'{aantalitems}'
def aantalmin():
        global aantalitems
        aantalitems -= 1


while True:
    aantalitems = 10
    Aantal = Label(Window,bg='yellow',text=f'{aantalitems}')
    Aantal.pack(ipadx=5,ipady=30,fill='both')

    button = Button(Window,text='Grabbelen')

    button.config(command=lambda:[gekozen(),aantalitemtext(),aantalmin()])

    button.pack(ipadx=5,ipady=5,expand=True)

    Gekozenitem = Label(Window, bg='yellow')
    Gekozenitem.pack(ipadx=5,ipady=30,fill='both',side='bottom')
    aantalitems -= 1
    
    if len(Itemlijst) == 0:
        Window.destroy()
        break

    Window.mainloop()



