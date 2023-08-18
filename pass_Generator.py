from tkinter import *

import random,string

root =Tk()

root.geometry("400x280")

title = StringVar()

label = Label(root,textvariable=title).pack

title.set("The Strength Of Password")

def selecion():
    selecion = choice.get()
    
choice=IntVar()

R1=Radiobutton(root,text="Poor",variable=choice,value=1,command=selecion).pack(anchor=CENTER)
R2=Radiobutton(root,text="Average",variable=choice,value=2,command=selecion).pack(anchor=CENTER)
R3=Radiobutton(root,text="Advanced",variable=choice,value=3,command=selecion).pack(anchor=CENTER)

labelChoice = Label(root)
labelChoice.pack()

lenlable= StringVar()
lenlable.set("Password Length:")

lentitle= Label(root,textvariable=lenlable).pack()


val = IntVar()
spinlenght = Spinbox(root,from_=8,to=24,textvariable=val,width=13).pack()



def callback():
    Isum.config(text= passgen())
    
passgenButton = Button(root,text="Genrate Password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

Isum = Label(root,text="")
Isum.pack(side=BOTTOM) 


poor = string.ascii_uppercase +string.ascii_lowercase

average = string.ascii_uppercase + string.ascii_lowercase + string.digits

symbols = """~!@#$%^&*()_+={}[]\\|:;<>,.?/"""

advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average,val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance,val.get()))
    
root.mainloop()
    