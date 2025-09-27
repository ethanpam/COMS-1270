#Ethan Pham        9-11-25
#Lab 2 - This code calculates a circle's circumfernece by multiplying 2 with pie and radius

import math

def circleCircumference(r):
    # Citation - https://www.khanacademy.org/a/radius-diameter-circumference
    # Citation - Author: Khan Academy
    # Citation - Date Published:2-12-2020 
    # Citation - Date Accessed: 9-11-25
    return 2 * math.pi * r

def main():
    radius = int(input("Enter the radius of the base: "))
    answer = circleCircumference(radius)
    print(f"Your circumference was {answer}")

if __name__ == "__main__":
    main()