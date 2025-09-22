#Ethan Pham        9-11-25
#Lab 2 - This code calcuates distance an object travels by using speed multipied by time

# Citation - https://studymind.co.uk/notes/calculating-distance-travelled/
# Citation - Author: Study Mind
# Citation - Date Posted: 9-21-2016
# Citation - Date Accessed: 9-11-25

import math

def dst(s, t):
    # Citation - https://studymind.co.uk/notes/calculating-distance-travelled/
    # Citation - Author: Study Mind
    # Citation - Date Posted: 9-21-2016
    # Citation - Date Accessed: 9-11-25
    return s * t

def main():
    speed = int(input("Enter speed in meters per second: "))
    time = int(input("Enter the time in seconds: "))
    answer = dst(speed, time)
    print(f"Your distance was {answer}")

if __name__ == "__main__":
    main()