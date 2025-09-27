# Ethan Pham        9-25-25        Lab B

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    while True:
        path = int(input("Which module would you like to enter? \n[1]myShapes \n[2]myPhysics \n[3]myOhmsLaw \n[4]myFinances\n"))
        if path == 1:
            section = int(input("Which section would you like to calculate? \n[1]areaOfRectangle \n[2]rectanglePerimeter \n[3]areaOfCircle \n[4]circleCircumference \n"))
            if section == 1:
                base = int(input("Enter the length of the base: "))
                height = int(input("Enter the height of the rectangle: "))
                answer = myShapes.areaOfRectangle(base, height)
                print(f"Your area was {answer}")
                break
            break

if __name__ == "__main__":
    main()