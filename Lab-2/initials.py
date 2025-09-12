#Ethan Pham        9-11-25
#Lab 2 - This code uses turtle to write a bubble letter of my first and last initals with a bunch of other twist such as background change and filling in the bubble letters with a different color

from turtle import Turtle #we can use its function

t = Turtle()

def f(v):
    t.forward(v)
def l(v):
    t.left(v)
def r(v):
    t.right(v)
t.screen.bgcolor("black")
t.speed(5)
t.pensize(10)
t.begin_fill()
t.pencolor("red")
t.fillcolor("violet")

t.goto(-100,0)
r(90)
f(200) #base huge line
l(90)
f(100) #bottom line for e
l(90)
f(20) #turn line
l(90)
f(70) #line
r(90)
f(60) #foward up?)
r(90)
f(70)
l(90)
f(20)
l(90)
f(70) 
r(90)
f(80)
r(90)
f(70)
l(90)
f(20)
t.end_fill()

t.begin_fill()
t.fillcolor("white")
r(90)
t.penup()
f(40)
r(90)
t.pencolor("blue")
t.pendown()
f(200)
l(90)
f(30)
l(90)
f(110)
r(90)
f(70)
l(90)
f(90)
l(90)
f(100)

t.end_fill()

t.screen.exitonclick() #keeps the screen active 
#t.screen.mainloop()