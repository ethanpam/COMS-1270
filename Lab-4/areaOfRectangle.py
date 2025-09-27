#Ethan Pham        9-11-25
#Lab 2 - This code finds the area of a rectangle by calculating its length and height

import math

def areaOfRectangle(b, h):
    # Citation - https://www.cuemath.com/measurement/area-of-rectangle/
    # Citation - Author: Cuemath
    # Citation - Date Published: 10-23-2021
    # Citation - Date Accessed: 9-11-25
    return b * h

def main():
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the rectangle: "))
    answer = areaOfRectangle(base, height)
    print(f"Your area was {answer}")

if __name__ == "__main__":
    main()