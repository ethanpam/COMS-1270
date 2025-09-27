#Ethan Pham        9-11-25
#Lab 2 - This code calculates perimeter by representing the total distance around with length + width multipied by 2

import math

def rectanglePerimeter(l, w):
    # Citation - https://www.smartick.com/blog/mathematics/geometry/how-to-calculate-perimeters-1/
    # Citation - Author: Smartick
    # Citation - Date Written - 6-3-2019
    # Citation - Date Accessed: 9-11-25
    return 2 * (l + w)

def main():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    answer = rectanglePerimeter(length, width)
    print(f"Your area was {answer}")

if __name__ == "__main__":
    main()