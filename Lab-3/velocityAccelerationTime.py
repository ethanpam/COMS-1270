#Ethan Pham        9-11-25
#Lab 2 - This code calculates the final velocity by using initial velocity, acceleration, and time 

# Citation - https://www.dummies.com/article/academics-the-arts/science/physics/how-to-calculate-time-and-distance-from-acceleration-and-velocity-174278/
# Citation - Author: Steven Holzner
# Citation - Date Written - 9-9-2021
# Citation - Date Accessed: 9-11-25

import math

def vat(i, a, t):
    # Citation - https://www.dummies.com/article/academics-the-arts/science/physics/how-to-calculate-time-and-distance-from-acceleration-and-velocity-174278/
    # Citation - Author: Steven Holzner
    # Citation - Date Written - 9-9-2021
    # Citation - Date Accessed: 9-11-25
    return i + (a * t)
def main():
    initial_v = int(input("Enter the initial velocity in meters per second: "))
    acceleration = int(input("Enter the acceleration in meters per second squared: "))
    time = int(input("Enter the time in seconds: "))
    answer = vat(initial_v, acceleration, time)
    print(f"Your final velocity was {answer}")

if __name__ == "__main__":
    main()