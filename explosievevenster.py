import tkinter

window = tkinter.Tk()

# def changebgW():
#     window['bg'] = 'white'
# def changebgR():
#     window['bg'] = 'red'
# def changebgY():
#     window['bg'] = 'yellow'
# def changebgB():
#     window['bg'] = 'blue'
# def changebgP():
#     window['bg'] = 'purple'
# def destroy():
#     window.destroy()
# def changewindow1():
#     window.geometry('250x250')
# def 
# def print5():
#     print(5)


# window.configure(bg = 'green')
# window.after(2000,changebgW)
# window.after(2000,changewindow1)
# window.after(2000,print5)

# window.after(4000,changebgY)
# window.after(4000,changewindow1)

# window.after(6000,changebgR)
# window.after(8000,changebgB)
# window.after(10000,changebgP)
# window.after(12000,destroy)

def colors1():
    window.configure(bg='red')
    window.geometry('250x250')
    print(5)
e = 2000
window.after(e,colors1)
def colors2():
    window.configure(bg='blue')
    window.geometry('300x300')
    print(4)
e += 2000
window.after(e,colors2)
def colors3():
    window.configure(bg='yellow')
    window.geometry('350x350')
    print(3)
e += 2000
window.after(e,colors3)
def colors4():
    window.configure(bg='purple')
    window.geometry('400x400')
    print(2)
e += 2000
window.after(e,colors4)
def colors5():
    window.configure(bg='green')
    window.geometry('450x450')
    print(1)
e += 2000
window.after(e,colors5)

def final():
    window.destroy()
    print('BOOM')
e+=2000
window.after(e,final)


window.mainloop()