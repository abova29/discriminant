import math
from tkinter import *
print("Введите уравнение вида ax²+bx+c=0")
a=int(input("Введите a>>"))
b=int(input("Введите b>>"))
c=int(input("Введите c>>"))
print("   ")
print("^^Введенные вами данные^^")
print("█████████████████████████")
print("↓↓Ответ       программы↓↓")

if a==0:
  print("a=",a,"  ██ bx+c=0")
  print("b=",b,"  ██",b,"*x+",c,"=0")
  print("c=",c,"  ██",b,"*x=-",c,)
  print("\n   ",  b)
  print("x=-----")
  print("  ", c)
  x= (-b)/c
  print("Ответ программы:\n")
  print("x=", x)

if b==0:
  print("ax²+c=0")
  print(a,"x²+",c,"=0")
  print(a,"x²=-(",c,")")
  print("\n   √-(",c,")")
  print("x=-----")
  print("   √", c)
  print("\nОтвет программы:")
  if c>0:
     print("Корней не существует!")
  if c<0:
     x=math.sqrt(-c / a)
     print("x=",x)
  

if c==0:
  print("ax²+bx=0")
  print(a,"x²+",b,"x=0")
  print("x(",a,"x+",b,")=0")
  x1=0
  print("x1=", x1 ," ██ ",a,"x+",b,"=0")
  print("       ██ ",a,"x=-",b,)
  print("\n              -",  b)
  print("           x2=-----")
  print("               ", a)
  x2= (-b)/a
  print("\nОтвет программы:")
  print("x1=",x1)
  print("x2=",x2)




else:
  D=b*b - 4 * a * c
  if D>0 and a!=0 and c<0 and b!=0:
      print("a=",a,"  ██ D=(",b,")²- 4*",a,"*",c,"=",D)
      print("b=",b,"  ██ x1,2= -b ± √D     -(",b,")±√",D)
      print("c=",c," ██       ------- = ----------------")
      print("                  2*a         2*",a         )
      x1=(-b+math.sqrt(D))/(2*a)
      x2=(-b-math.sqrt(D))/(2*a)
      print("   ")
      print("Ответ программы:")
      print("x1=",x1,)
      print("x2=",x2,)
  if D<0 and a!=0 and c<0 and b!=0:
      print("a=",a,"  ██ D=(",b,")²- 4*",a,"*",c,"=",D)
      print("b=",b,"  ██  Дискриминант(",D,") < 0")
      print("c=",c,"  ██   Корней не существует!")
      print("   ")
      print("Ответ программы:")
      print("Корней не существует!")
  if D==0 and a!=0 and c<0 and b!=0:
      print("a=",a,"  ██ D=(",b,")²- 4*",a,"*",c,"=",D)
      print("b=",b,"  ██ x1,2= -b ± √D     -(",b,")±√",D)
      print("c=",c," ██       ------- = ----------------")
      print("                  2*a         2*",a         )
      x=(-b+math.sqrt(D))/(2*a)
      print("   ")
      print("Ответ программы:")
      print("x=",x)

print("   ")
print("   ")
print("Код был написан группой людей на бесплатной основе...")
print("Мы не будем против, если вы поддержите нас денюжкой.")
print(" ")
print("Мы в ВК: https://vk.com/serving_antifem")

