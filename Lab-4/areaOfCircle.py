#Ethan Pham        9-11-25
#Lab 2 - This code uses the radius of a circle multipied by pi to find its area

import math

def areaOfCircle(r):
    # Citation - https://www.khanacademy.org/math/8th-grade-foundations-engageny/8th-m5-engage-ny-foundations/8th-m5-tb-foundations/a/area-of-a-circle
    # Citation - Author: Khan Academy
    # Citation - Date Published: 12-23-2019
    # Citation - Date Accessed: 9-11-25
    return math.pi * (r ** 2)

def main():
    radius = int(input("Enter the radius of the circle: "))
    answer = areaOfCircle(radius)
    print(f"Your area was {answer}")

if __name__ == "__main__":
    main()