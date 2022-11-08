from tkinter import *
import math
import tkinter.messagebox
root=Tk()
root.geometry('650x400+300+300')
root.title("Scientific Calculator")
switch=None
def btn_1():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'1')
def btn_2():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'2')
def btn_3():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'3')
def btn_4():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'4')
def btn_5():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'5')
def btn_6():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'6')
def btn_7():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'7')
def btn_8():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'8')
def btn_9():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,'9')


def btn_0():
    if screen.get() == '0':
        screen.delete(0, END)
    pos = len(screen.get())
    screen.insert(pos, '0')

def pi():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,str(math.pi))

def exp():
    if screen.get()=='0':
        screen.delete(0,END)
    pos=len(screen.get())
    screen.insert(pos,str(math.e))

def btn_p():
    pos = len(screen.get())
    screen.insert(pos, '+')

def btn_s():

    pos = len(screen.get())
    screen.insert(pos, '-')

def btn_ml():

    pos = len(screen.get())
    screen.insert(pos, '*')

def btn_di():

    pos = len(screen.get())
    screen.insert(pos, '/')

def sin():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def cos():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def tan():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")


def asin():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.asin(math.radians(ans))
        else:
            ans=math.asin(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def acos():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.acos(math.radians(ans))
        else:
            ans=math.acos(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def atan():
    try:
        ans=float(screen.get())
        if switch is True:
            ans=math.atan(math.radians(ans))
        else:
            ans=math.atan(ans)
            screen.delete(0, END)
            screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def log():
    try:
        ans=float(screen.get())
        ans=math.log10(ans)
        screen.delete(0, END)
        screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def ln():
    try:
        ans=float(screen.get())
        ans=math.log(ans)
        screen.delete(0, END)
        screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")

def fact():
    try:
        ans=float(screen.get())
        ans=math.factorial(ans)
        screen.delete(0, END)
        screen.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error!")


def pow():
    pos=len(screen.get())
    screen.insert(pos,"**")
def dot():
    pos=len(screen.get())
    screen.insert(pos,".")
def br():
    pos=len(screen.get())
    screen.insert(pos,"(")
def bl():
    pos=len(screen.get())
    screen.insert(pos,")")
def cl():
    pos=len(screen.get())
    screen.delete(0,END)
    screen.insert(pos,"0")
def mod():
    pos=len(screen.get())
    screen.insert(pos,"%")
def dele():
    ans=screen.get()
    pos = ans[:len(screen.get())-1]
    screen.delete(0,END)
    screen.insert(0,pos)


def eq():
    ans=screen.get()
    ans=eval(ans)
    screen.delete(0,END)
    screen.insert(0,ans)


screen= Entry(root,font='Verdana 20',fg="Black",bd=4,bg="#758168",justify=RIGHT)
screen.insert(0,"0")
screen.pack(fill=BOTH,expand=TRUE)

f= Frame(root,bg="#000000")



pib=Button(f, text="π",font="segoe 18",command=pi,bd=0,relief=GROOVE)
pib.pack(side=LEFT,expand=TRUE,fill=BOTH)


factb=Button(f, text="x!",font="segoe 18",command=fact,bd=0,relief=GROOVE)
factb.pack(side=LEFT,expand=TRUE,fill=BOTH)


sinb=Button(f, text="sin",font="segoe 18",command=sin,bd=0,relief=GROOVE)
sinb.pack(side=LEFT,expand=TRUE,fill=BOTH)


cosb=Button(f, text="cos",font="segoe 18",command=cos,bd=0,relief=GROOVE)
cosb.pack(side=LEFT,expand=TRUE,fill=BOTH)


tanb=Button(f, text="tan",font="segoe 18",command=tan,bd=0,relief=GROOVE)
tanb.pack(side=LEFT,expand=TRUE,fill=BOTH)


oneb=Button(f, text="1",font="segoe 23",command=btn_1,bd=0,relief=GROOVE)
oneb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)


twob=Button(f, text="2",font="segoe 23",command=btn_2,bd=0,relief=GROOVE)
twob.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

threeb=Button(f, text="3",font="segoe 23",command=btn_3,bd=0,relief=GROOVE)
threeb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

plusb=Button(f, text="+",font="segoe 23 bold",command=btn_p,bd=0,relief=GROOVE)
plusb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)
f.pack(fill=BOTH,expand=TRUE)




f= Frame(root,bg="#000000")


e_b=Button(f, text="e",font="segoe 18",command=exp,bd=0,relief=GROOVE)
e_b.pack(side=LEFT,expand=TRUE,fill=BOTH)


rootb=Button(f, text="√x",font="segoe 18",bd=0,relief=GROOVE)
rootb.pack(side=LEFT,expand=TRUE,fill=BOTH)
rootb.bind("<Button-1>")

sinhb=Button(f, text="sin-1",font="segoe 18",command=asin,bd=0,relief=GROOVE)
sinhb.pack(side=LEFT,expand=TRUE,fill=BOTH)


coshb=Button(f, text="cos-1",font="segoe 18",command=acos,bd=0,relief=GROOVE)
coshb.pack(side=LEFT,expand=TRUE,fill=BOTH)


tanhb=Button(f, text="tan-1",font="segoe 18",command=atan,bd=0,relief=GROOVE)
tanhb.pack(side=LEFT,expand=TRUE,fill=BOTH)


fourb=Button(f, text="4",font="segoe 23",command=btn_4,bd=0,relief=GROOVE)
fourb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)


fiveb=Button(f, text="5",font="segoe 23",command=btn_5,bd=0,relief=GROOVE)
fiveb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

sixb=Button(f, text="6",font="segoe 23",command=btn_6,bd=0,relief=GROOVE)
sixb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

minusb=Button(f, text="-",font="segoe 27 bold",command=btn_s,bd=0,relief=GROOVE)
minusb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)
f.pack(fill=BOTH,expand=TRUE)

f= Frame(root,bg="orange")


Radb=Button(f, text="Rad",font="segoe 12 bold",bd=0,relief=GROOVE)
Radb.pack(side=LEFT,expand=TRUE,fill=BOTH)


Roundb=Button(f, text="round",font="segoe 10 bold",bd=0,relief=GROOVE)
Roundb.pack(side=LEFT,expand=TRUE,fill=BOTH)
Roundb.bind("<Button-1>")

ln_b=Button(f, text="ln",font="segoe 18",command=ln,bd=0,relief=GROOVE)
ln_b.pack(side=LEFT,expand=TRUE,fill=BOTH)


logb=Button(f, text="log",font="segoe 18",command=log,bd=0,relief=GROOVE)
logb.pack(side=LEFT,expand=TRUE,fill=BOTH)


powb=Button(f, text="x^y",font="segoe 18",command=pow,bd=0,relief=GROOVE)
powb.pack(side=LEFT,expand=TRUE,fill=BOTH)


sevenb=Button(f, text="7",font="segoe 23",command=btn_7,bd=0,relief=GROOVE,fg='black',bg='white')
sevenb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)


eightb=Button(f, text="8",font="segoe 23",command=btn_8,bd=0,relief=GROOVE)
eightb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

nineb=Button(f, text="9",font="segoe 23",command=btn_9,bd=0,relief=GROOVE)
nineb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

intob=Button(f, text="*",font="segoe 23 bold",command=btn_ml,bd=0,relief=GROOVE)
intob.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)
f.pack(expand=TRUE,fill=BOTH)


f= Frame(root,bg="grey")


perb=Button(f, text="%",font="segoe 18 bold",command=mod,bd=0,relief=GROOVE)
perb.pack(side=LEFT,expand=TRUE,fill=BOTH)


brac1b=Button(f, text="(",font="segoe 18",command=br,bd=0,relief=GROOVE)
brac1b.pack(side=LEFT,expand=TRUE,fill=BOTH)


brac2b=Button(f, text=")",font="segoe 18",command=bl,bd=0,relief=GROOVE)
brac2b.pack(side=LEFT,expand=TRUE,fill=BOTH)


dotb=Button(f, text=".",font="segoe 23 bold",command=dot,bd=0,relief=GROOVE)
dotb.pack(side=LEFT,expand=TRUE,fill=BOTH)


allclearb=Button(f, text="AC",font="segoe 23 bold",command=cl,bd=0,relief=GROOVE,fg='red')
allclearb.pack(side=LEFT,expand=TRUE,fill=BOTH)


delb=Button(f, text="⌦",font="segoe 25 bold",command=dele,bd=0,relief=GROOVE,fg='red')
delb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)


zerob=Button(f, text="0",font="segoe 23",command=btn_0,bd=0,relief=GROOVE)
zerob.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

equalb=Button(f, text="=",font="segoe 23 bold",command=eq,bd=0,relief=GROOVE)
equalb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)

divideb=Button(f, text="/",font="segoe 23 bold",command=btn_di,bd=0,relief=GROOVE)
divideb.pack(side=LEFT,expand=TRUE,fill=BOTH)
# b.bind("<Button-1>",click)
f.pack(expand=TRUE,fill=BOTH)
root.mainloop()