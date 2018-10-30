import turtle
from turtle import *
from random import randint

amount = input("Max 4 zolwie, ile chcesz miec?: ")
input("Wybrałeś " + amount + " żółwi. Naciśnij odpowiedni przyciszk aby przesunąć swojego żółwia.\n"
                             "Od góry q,r,y lub p. Później naciśnj byle co by przejsc do gry")

speed(1000)
penup()
goto(-140,140)
pendown()


for step in range(11):
    write(step)
    right(90)
    for i in range(8):
        forward(10)
        penup()
        forward(10)
        pendown()
    penup()
    backward(160)
    left(90)
    forward(20)
    pendown()

wn = turtle.Screen()


if amount == '1':
    oliwia = Turtle()
    oliwia2 = Turtle()
    oliwia3 = Turtle()
    patryk = Turtle()
    oliwia.color('red')
    oliwia.shape('turtle')
    oliwia.penup()
    oliwia.goto(-160, 100)
    oliwia.pendown()
elif amount == '2':
    oliwia = Turtle()
    oliwia2 = Turtle()
    oliwia3 = Turtle()
    oliwia.color('red')
    oliwia.shape('turtle')
    oliwia.penup()
    oliwia.goto(-160, 100)
    oliwia.pendown()
    patryk = Turtle()
    patryk.color('blue')
    patryk.shape('turtle')
    patryk.penup()
    patryk.goto(-160, 80)
    patryk.pendown()
elif amount == '3':
    oliwia = Turtle()
    oliwia.color('red')
    oliwia.shape('turtle')
    oliwia.penup()
    oliwia.goto(-160, 100)
    oliwia.pendown()
    patryk = Turtle()
    patryk.color('blue')
    patryk.shape('turtle')
    patryk.penup()
    patryk.goto(-160, 80)
    patryk.pendown()
    oliwia2 = Turtle()
    oliwia2.color('yellow')
    oliwia2.shape('turtle')
    oliwia2.penup()
    oliwia2.goto(-160, 60)
    oliwia2.pendown()
    oliwia2 = Turtle()
    patryk = Turtle()
elif amount == '4':
    oliwia = Turtle()
    oliwia.color('red')
    oliwia.shape('turtle')
    oliwia.penup()
    oliwia.goto(-160, 100)
    oliwia.pendown()
    patryk = Turtle()
    patryk.color('blue')
    patryk.shape('turtle')
    patryk.penup()
    patryk.goto(-160, 80)
    patryk.pendown()
    oliwia2 = Turtle()
    oliwia2.color('yellow')
    oliwia2.shape('turtle')
    oliwia2.penup()
    oliwia2.goto(-160, 60)
    oliwia2.pendown()
    oliwia3 = Turtle()
    oliwia3.color('pink')
    oliwia3.shape('turtle')
    oliwia3.penup()
    oliwia3.goto(-160, 40)
    oliwia3.pendown()

stop = True


def h1():
        if (patryk.xcor() >= 60) or (oliwia2.xcor() >= 60) or (oliwia3.xcor() >= 60):
            oliwia.forward(0)
        elif oliwia.xcor() < 60:
            oliwia.forward(5)
        elif oliwia.xcor() >= 60:
            oliwia.write("WYGRALAS")

def h2():

    if (oliwia.xcor() >= 60) or (oliwia2.xcor() >= 60) or (oliwia3.xcor() >= 60):
        patryk.forward(0)
    elif patryk.xcor() < 60:
        patryk.forward(5)
    elif patryk.xcor() >= 60:
        patryk.write("WYGRALAS")

def h3():
    if (patryk.xcor() >= 60) or (oliwia.xcor() >= 60) or (oliwia3.xcor() >= 60):
        oliwia2.forward(0)
    elif oliwia2.xcor() < 60:
        oliwia2.forward(5)
    elif oliwia2.xcor() >= 60:
        oliwia2.write("WYGRALAS")

def h4():
    if (patryk.xcor() >= 60) or (oliwia2.xcor() >= 60) or (oliwia.xcor() >= 60):
        oliwia3.forward(0)
    elif oliwia3.xcor() < 60:
        oliwia3.forward(5)
    elif oliwia3.xcor() >= 60:
        oliwia3.write("WYGRALAS")





wn.onkey(h1,'q')
wn.onkey(h2,'r')
wn.onkey(h3,'y')
wn.onkey(h4,'p')
print(oliwia.xcor())


wn.listen()
wn.mainloop()





