from tkinter import*
import random
import string
import pyperclip


def btn_click():
    test = pas
    pyperclip.copy(test)

pas = ''
for x in range(16): 
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!?&'))

root = Tk()

root['bg'] = '#fafafa'
root.title('Password generator')
root.geometry('300x250')

Canvas = Canvas(root, height=300, width=250)
Canvas.pack()

Frame = Frame(root, bg='white')
Frame.place(relwidth=1, relheight=1)

title = Label(Frame, text= pas)
title.pack()
regen = Button(Frame, text='New password', bg='white')
regen.pack
btn = Button(Frame, text='Copy', bg='white', command=btn_click)
btn.pack()

root.mainloop()