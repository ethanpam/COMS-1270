#Ethan Pham        9-11-25
#Lab 2 - This code calculates voltage by measuring the current mulitipied by its resistence

import math

def cv(c, r):
    # Citation - https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    # Citation - Author: All About Circuits
    # Citation - Data Published: 4-16-2020
    # Citation - Date Accessed: 9-11-25
    return c * r

def main():
    current = int(input("Enter the current: "))
    resistence = int(input("Enter the resistence: "))
    answer = cv(current, resistence)
    print(f"Your voltage was {answer}")

if __name__ == "__main__":
    main()