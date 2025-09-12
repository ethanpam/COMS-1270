#Ethan Pham        9-11-25
#Lab 2 - This code calculates resistence by using Ohm's formula by dividing voltage with current

# Citation - https://courses.lumenlearning.com/suny-physics/chapter/20-3-resistance-and-resistivity/
# Citation - Author: Lumen Learning
# Citation - Date Published: 4-25-2023
# Citation - Date Accessed: 9-11-25

import math

current = int(input("Enter the current: "))
voltage = int(input("Enter the voltage: "))

answer = voltage/current

print(f"Your resistance was {answer}")