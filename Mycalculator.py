from tkinter import *


exp=""

#methods
def click(a):
	global exp
	exp = exp+a
	e.set(exp) 
def eclick():
	global exp
	exp = str(eval(exp))
	e.set(exp)
	


#frame
r = Tk()
r.title("Calculator")
r.geometry("475x700")

b1 = Button(r,text="1",font="times 48",width=3,command=lambda:click("1"))
b1.grid(row=1,column=0)
b2 = Button(r,text="2",font="times 48",width=3,command=lambda:click("2"))
b2.grid(row=1,column=1)
b3 = Button(r,text="3",font="times 48",width=3,command=lambda:click("3"))
b3.grid(row=1,column=2)
b4 = Button(r,text="4",font="times 48",width=3,command=lambda:click("4"))
b4.grid(row=2,column=0)
b5 = Button(r,text="5",font="times 48",width=3,command=lambda:click("5"))
b5.grid(row=2,column=1)
b6 = Button(r,text="6",font="times 48",width=3,command=lambda:click("6"))
b6.grid(row=2,column=2)
b7 = Button(r,text="7",font="times 48",width=3,command=lambda:click("7"))
b7.grid(row=3,column=0)
b8 = Button(r,text="8",font="times 48",width=3,command=lambda:click("8"))
b8.grid(row=3,column=1)
b9 = Button(r,text="9",font="times 48",width=3,command=lambda:click("9"))
b9.grid(row=3,column=2)
b0 = Button(r,text="0",font="times 48",width=3,command=lambda:click("0"))
b0.grid(row=4,column=1)
subtract = Button(r,text="-",font="times 48",width=3,command=lambda:click("-"))
subtract.grid(row=4,column=0)
add = Button(r,text="+",font="times 48",width=3,command=lambda:click("+"))
add.grid(row=4,column=2)
equal = Button(r,text ="=",font="times 48",width=3,command=lambda:eclick())
equal.grid(row=1,column=3)
divide = Button(r,text ="/",font="times 48",width=3,command=lambda:click("/"))
divide.grid(row=2,column=3)
multiply = Button(r,text ="*",font="times 48",width=3,command=lambda:click("*"))
multiply.grid(row=3,column=3)
mod = Button(r,text ="%",font="times 48",width=3,command=lambda:click("%"))
mod.grid(row=4,column=3)
e = StringVar()
e.set("")
display = Entry(r,textvariable=e,width=27,font="times 48")
display.grid(row=0,columnspan=120,ipadx=70)
r.mainloop()