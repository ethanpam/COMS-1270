# Ethan Pham      10-9-25
# This application uses the L-System rule to act in strange ways like a cell
# Citation - #https://runestone.academy/ns/books/published/iowastateuniversity_thinkcspy_fall25/Strings/TurtlesandStringsandLSystems.html
# Citation - Runestone Academy
# Citation - Date Accessed: 10-11-25
#some idea reread 9.15 p means randomly placing ur turtle so we can use t.goto(rand(0-200,200), y(-200,200)
import tridecagonTurtle
import turtle
import random

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F+P+T+F-F-B'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            tridecagonTurtle.tridecagonTurtle(distance, aTurtle.xcor(), aTurtle.ycor(), aTurtle)
        elif cmd == "P":
            x = random.randint(-300,300)
            y = random.randint(-300,300)
            aTurtle.penup()
            aTurtle.goto(x,y)
            aTurtle.pendown()

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(20)
    drawLsystem(t, inst, 60, 20)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()