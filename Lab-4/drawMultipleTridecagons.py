#Ethan Pham         9-24-25         Lab B
#This draws a multiple tridecagon on a certain position depending on the users input including the size of the tridecagon with the user's input on the length of each side
#Source: https://artofproblemsolving.com/wiki/index.php/Tridecagon?srsltid=AfmBOoo-Qrx8eZG0TydU2iTSgsjKvFb_PnfPdPkzUk15PriP1I2F5oCH

from turtle import Turtle

def drawMultipleTridecagons(s, x, y, nr, sr, t):
    t.penup()
    t.goto(x,y)
    for p in range(nr):
        t.penup()
        t.setx(x + p * sr)
        tridecagonTurtle(s, t)
        t.penup()

def tridecagonTurtle(s, t):
    degree = (360/13)
    for i in range(13):
        t.pendown()
        t.forward(s)
        t.left(degree)


def main():
    s = int(input("Enter each side length of the tridecagon: "))
    x = int(input("Enter the x-coordinate of the vertex: "))
    y = int(input("Enter the y-coordinate of the vertex: "))
    nr = int(input("How many tridecagons would you like to draw? "))
    sr = int(input("What is the space between tridecagon on the 'x' axis: "))
    t = Turtle()
    drawMultipleTridecagons(s, x, y, nr, sr, t)
    t.screen.exitonclick()

if __name__ == "__main__":
    main()