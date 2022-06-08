from tkinter import *

top = Tk()
top.title('Calculadora 1.0')
top.geometry("350x430")
top.resizable(0,0)
top.configure(bg='black')

#-----------------------------------FUNCIONES--------------------------------------
def btn_click(input):
    global expression
    expression = expression + str(input)
    input_text.set(expression)

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)

def clear():
    global expression
    expression = ""
    input_text.set("")

#-------------------------------------Display-------------------------------------
expression = ""
input_text = StringVar()

display = Entry(top,relief=RIDGE,bd=9,width=11,font=('arial',38,'bold'),fg='white',bg='#CBCBCB',textvariable = input_text,justify=RIGHT).place(x=13,y=14)

#-------------------------------------Botones-------------------------------------
clear_button = Button(top,text='C',width=4,fg='white',bg='red',font=('',20,'bold'),command = lambda : clear()).place(x=13,y= 100)
multiply_button = Button(top,text='X',width=4,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_click("*")).place(x=96,y= 100)
divide_button = Button(top,text='/',width=4,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_click("/")).place(x=179,y= 100)
star_button = Button(top,text='*',width=4,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_click("*")).place(x=262,y= 100)
seven_button = Button(top,text='7',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("7")).place(x=13,y=165)
eight_button = Button(top,text='8',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("8")).place(x=96,y= 165)
nine_button = Button(top,text='9',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("9")).place(x=179,y= 165)
minus_button = Button(top,text='-',width=4,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_click("-")).place(x=262,y= 165)
four_button = Button(top,text='4',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("4")).place(x=13,y= 230)
five_button = Button(top,text='5',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("5")).place(x=96,y= 230)
six_button = Button(top,text='6',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("6")).place(x=179,y= 230)
plus_button = Button(top,text='+',width=4,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_click("+")).place(x=262,y= 230)
one_button = Button(top,text='1',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("1")).place(x=13,y= 295)
two_button = Button(top,text='2',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("2")).place(x=96,y= 295)
three_button = Button(top,text='3',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("3")).place(x=179,y= 295)
equal_button = Button(top,text='=',width=4,height=3,fg='white',bg='orange',font=('',20,'bold'),command = lambda : btn_equal()).place(x=262,y= 295)
zero_button = Button(top,text='0',width=9,height=1,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click("0")).place(x=13,y= 360)
dot_button = Button(top,text='.',width=4,fg='white',bg='#3F3F3F',font=('',20,'bold'),command = lambda : btn_click(".")).place(x=179,y= 360)


top.mainloop()
