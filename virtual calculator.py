import tkinter
from tkinter import *
from tkinter import messagebox

win=tkinter.Tk()
win.geometry("250x400+300+300")
win.resizable(0,0)
win.title("CALCULATOR")

val=""
A=0
operator=""

def bton_one_pressed():
    global val
    val=val + "1"
    data.set(val)
    
def bton_two_pressed():
    global val
    val=val + "2"
    data.set(val)
    
def bton_three_pressed():
    global val
    val=val + "3"
    data.set(val)
    
def bton_four_pressed():
    global val
    val=val + "4"
    data.set(val)
    
def bton_five_pressed():
    global val
    val=val + "5"
    data.set(val)
    
def bton_six_pressed():
    global val
    val=val + "6"
    data.set(val)
    
def bton_seven_pressed():
    global val
    val=val + "7"
    data.set(val)
    
def bton_eight_pressed():
    global val
    val=val + "8"
    data.set(val)
    
def bton_nine_pressed():
    global val
    val=val + "9"
    data.set(val)
    
def bton_zero_pressed():
    global val
    val=val + "0"
    data.set(val)
    
def bton_plus_pressed():
    global val
    global A
    global operator
    A=int(val)
    operator="+"
    val=val + "+"
    data.set(val)
    
def bton_minus_pressed():
    global val
    global A
    global operator
    A=int(val)
    operator="-"
    val=val + "-"
    data.set(val)
    
    
def bton_mul_pressed():
    global val
    global A
    global operator
    A=int(val)
    operator="*"
    val=val + "*"
    data.set(val)
    
def bton_div_pressed():
    global val
    global A
    global operator
    A=int(val)
    operator="/"
    val=val + "/"
    data.set(val)

def c_pressed():
    global val
    global A
    global operator
    A=""
    val=""
    operator=""
    data.set(val)
    
def result():
    global val
    global A
    global operator
    val2=val
    if operator=="+":
        x=int(val2.split("+")[1])
        c=A + x
        data.set(c)
        val=str(c)
         
    elif operator=="-":
        x=int(val2.split("-")[1])
        c=A - x
        data.set(c)
        val=str(c)
        
    elif operator=="*":
        x=int(val2.split("*")[1])
        c=A * x
        data.set(c)
        val=str(c)
        
    elif operator=="/":
        x=int(val2.split("/")[1])
        if x==0:
            messagebox.showerror("Error","cant divisible by zero")
            A=0
            val=""
            oerator=""
        else:
            c=int(A / x)
            data.set(c)
            val= str(c)
        
    
 
    
            
            
        
    
    
    

data = StringVar()

lbl=Label(win,
          text="Label",
          anchor=SE,
          textvariable= data,
          font=("verdana",20),
)
lbl.pack(expand=True,fill="both",)

row1=Frame(win,bg="#000000")
row1.pack(expand=True,fill="both",)

row2=Frame(win)
row2.pack(expand=True,fill="both",)

row3=Frame(win)
row3.pack(expand=True,fill="both",)

row4=Frame(win)
row4.pack(expand=True,fill="both",)


bton1=Button(
        row1,
        text="1",
        font=("verdana",22),
        relief=GROOVE,
        border=0,
        command=bton_one_pressed
)
bton1.pack(side=LEFT,expand=True,fill="both")

bton2=Button(row1,
             text="2",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
              command=bton_two_pressed
)
bton2.pack(side=LEFT,expand=True,fill="both")

bton3=Button(row1,
             text="3",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
                 command=bton_three_pressed
)
bton3.pack(side=LEFT,expand=True,fill="both")

bton4=Button(row1,
             text="+",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
                 command=bton_plus_pressed
)
bton4.pack(side=LEFT,expand=True,fill="both")

bton1=Button(row2,
             text="4",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
                 command=bton_four_pressed
)
bton1.pack(side=LEFT,expand=True,fill="both")

bton2=Button(row2,
             text="5",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
                 command=bton_five_pressed
)
bton2.pack(side=LEFT,expand=True,fill="both")

bton3=Button(row2,
             text="6",
             font=("verdana",22),
              relief=GROOVE,
              border=0,
                 command=bton_six_pressed
)
bton3.pack(side=LEFT,expand=True,fill="both")

bton4=Button(row2,
             text="-",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_minus_pressed
)
bton4.pack(side=LEFT,expand=True,fill="both")

bton1=Button(row3,
             text="7",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_seven_pressed
)
bton1.pack(side=LEFT,expand=True,fill="both")

bton2=Button(row3,
             text="8",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_eight_pressed
)
bton2.pack(side=LEFT,expand=True,fill="both")

bton3=Button(row3,
             text="9",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_nine_pressed
)
bton3.pack(side=LEFT,expand=True,fill="both")

bton4=Button(row3,
             text="*",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_mul_pressed
)
bton4.pack(side=LEFT,expand=True,fill="both")

bton1=Button(row4,
             text="c",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=c_pressed
)
bton1.pack(side=LEFT,expand=True,fill="both")

bton2=Button(row4,
             text="0",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_zero_pressed
)
bton2.pack(side=LEFT,expand=True,fill="both")

bton3=Button(row4,
             text="=",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=result
)
bton3.pack(side=LEFT,expand=True,fill="both")

bton3=Button(row4,
             text="/",
             font=("verdana",22),
              relief=GROOVE,
        border=0,
           command=bton_div_pressed
)
bton3.pack(side=LEFT,expand=True,fill="both")

win.mainloop()