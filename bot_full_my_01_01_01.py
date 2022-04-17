from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Решить уравнение')
window.geometry("580x400")

frame = Frame( window )
entry  = Entry( frame )


def dialog():
    box.showinfo("Greetins","Welcome " + entry.get())
btn = Button(frame,text = "Enter Name", command = dialog )
#btn.pack( side = RIGHT , padx = 5)
#entry.pack( side = LEFT)
#frame.pack (padx = 20, pady = 20)

Calculate_Root_Equation = Label( window , text = "Вычислить Корень Уравнения", justify = CENTER)
Of_the_form = Label( window , text = "вида ax^2+bx+c=0", justify = CENTER)
Calculate_Root_Equation.grid(padx = 200, pady = 0)
Of_the_form.grid(padx = 200, pady = 0)
Exaple = Label( window , text = "Пример 2x^2+3x+4=0", justify = CENTER)
Exaple.grid(padx = 200, pady = 0)

viev_a = Label( window , text = "a =")
viev_a.grid(padx = 12 ,pady = 11)


viev_b = Label( window , text = "b =")
viev_b.grid()

viev_c = Label( window , text = "c =")
viev_c.grid()

#x1= ""
#x2= ""
#x = ""


frame1 = Frame( window )
frame2 = Frame( window )
frame3 = Frame( window )
entry1 = Entry( frame1 )
entry2 = Entry( frame2 )
entry3 = Entry( frame3 )
def dialog1():
    box.showinfo("Greetins","Welcome " + entry1.get())
    

entry1.grid(padx = 10,pady = 5)
frame1.grid(padx = 0,pady = 5)
##frame1.grid(padx = 50, pady = 50)

def dialog2():
    box.showinfo("Greetins","Welcome " + entry2.get())
##entry2.grid(padx = 40, pady = 40)
##frame2.grid(padx = 40, pady = 40)

entry2.grid( padx = 10, pady = 5)
frame2.grid(padx = 0, pady = 15)

def dialog3():
    box.showinfo("Greetins","Welcome " + entry3.get())
    
##entry3.grid( side = LEFT)
##frame3.grid(padx = 30, pady = 30)

entry3.grid(padx = 10, pady = 5)
frame3.grid(padx = 0,pady = 15)


new_poram = Button ( window )
new_poram.configure(text = "Решить", state = NORMAL) #, command = res_0

res = Button ( window )
res.configure(state = DISABLED)



label1 = Label( window, relief = 'groove', width = 2 )
label2 = Label( window, relief = 'groove', width = 2 )
label3 = Label( window, relief = 'groove', width = 2 )
label4 = Label( window, relief = 'groove', width = 2 )
label5 = Label( window, relief = 'groove', width = 2 )
label6 = Label( window, relief = 'groove', width = 2 )
label7 = Label( window, relief = 'groove', width = 2 )
label8 = Label( window, relief = 'groove', width = 2 )

def seek_a():
    btn1.configure(state = DISABLED)
    entry.get = a
def seek_b():
    btn2.configure(state = DISABLED)
    entry.get = b
def seek_c():
    btn3.configure(state = DISABLED)
    entry.get = c
def res_0():
     res.configure(state = DISABLED)
#     res.configure(state = NORMAL )
     new_poram.configure(state = NORMAL )
     entry1.config(state="normal")#разблокируем
     entry2.config(state="normal")#разблокируем
     entry3.config(state="normal")#разблокируем
def new_porametr():
    res.configure(state = NORMAL)
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    new_poram.configure(state = DISABLED )
    if( entry1['state']=='normal'):
        entry1.config(state="readonly")#блокируем
        #button.config(text="Разблокировать")
    #else:
        #entry1.config(state="normal")#разблокируем
        #button.config(text="Заблокировать")
    if( entry2['state']=='normal'):
        entry2.config(state="readonly")#блокируем
    if( entry3['state']=='normal'):
        entry3.config(state="readonly")#блокируем

    global a
    global b
    global c

    import math
    global x1
    a = float(a)
    b = float(b)
    c = float(c)
    sample = ("█████████████████████████\n↓↓Ответ       программы↓↓")
    if a==0:
      x= (-b)/c
    if b==0:
      if c>0:
         x = ("Корней не существует!")
      if c<0:
         x=math.sqrt(-c / a)
    if c==0:
         x=0
         x1= (-b)/a

    else:
     D = b*b - 4 * a * c
    if D>0 and a!=0 and c<0 and b!=0:
        x=(-b+math.sqrt(D))/(2*a)
        x1=(-b-math.sqrt(D))/(2*a)
    if D<0 and a!=0 and c<0 and b!=0:
        x = ("Корней не существует!")
    if D==0 and a!=0 and c<0 and b!=0:
        x=(-b+math.sqrt(D))/(2*a)
        otvet.grid()
    if x1 == (""):
      otvet.configure(text = "Ответ программы:"+x)
      otvet.grid()
    if x1 != (""):
      x_and_x1 = ("x1=",x,"\nx2=",x1)
      otvet.configure(text = "Ответ программы:"+x_and_x1)
      otvet.grid()

##
####label1.grid()
####label2.grid()
####label3.grid()
####label4.grid()
####label5.grid()
####label6.grid()
####label7.grid()
####label8.grid()






new_poram = Button ( window )
new_poram.configure(text = "Решить", state = NORMAL, command = new_porametr) #, command = res_0
res.configure (text = "Reset", command = res_0) 

viev_a.grid()
viev_b.grid()
viev_c.grid()
##viev_a.grid( padx = 5 ,pady = 20)
##viev_b.grid( padx = 10 ,pady = 20)
##viev_c.grid( padx = 15 ,pady = 20)


#justify = CENTER
Calculate_Root_Equation.grid()
Of_the_form.grid()
new_poram.grid()
##res.grid(padx = 30 ,pady = 30)
res.grid()






window.mainloop()


# Тио реклама - https://docs.google.com/spreadsheets/d/1_TeLiccac52qnzdkMT2WOG5ai4BxLRPP0u3ZNtjRVMc/edit
#print("Код был написан группой людей на бесплатной основе...")
#print("Мы не будем против, если вы поддержите нас денюжкой.")
#print(" ")
#print("Мы в ВК: https://vk.com/serving_antifem")
