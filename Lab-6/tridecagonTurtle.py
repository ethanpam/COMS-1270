#Ethan Pham         9-24-25         Lab B
#This draws a tridecagon on a certain vertex depending on the users input including the size of the tridecagon with the user's input on the length of each side
#Source: https://artofproblemsolving.com/wiki/index.php/Tridecagon?srsltid=AfmBOoo-Qrx8eZG0TydU2iTSgsjKvFb_PnfPdPkzUk15PriP1I2F5oCH

from turtle import Turtle

def tridecagonTurtle(s, x, y, t):
    degree = (360/13)

    t.penup()
    t.goto(x,y)
    t.pendown()

    for i in range(13):
        t.forward(s)
        t.left(degree)

def main():
    s = int(input("Enter each side length of the tridecagon: "))
    x = int(input("Enter the x-coordinate of the vertex: "))
    y = int(input("Enter the y-coordinate of the vertex: "))
    t = Turtle()
    tridecagonTurtle(s, x, y, t)
    t.screen.exitonclick()

if __name__ == "__main__":
    main()