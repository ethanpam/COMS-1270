#Ethan Pham        9-11-25
#Lab 2 - This code uses Ohm's law to calculate current as current is directly proportional to the voltage across the board, given current is voltage divided by resistence
# Citation - https://study.com/skill/learn/how-to-calculate-the-current-in-an-electric-circuit-using-ohms-law-explanation.html#:~:text=Steps%20for%20Calculating%20the%20Current,resistance%20found%20in%20step%201.
# Citation - Author: Study
# Citation - Date Published: 3-22-25
# Citation - Date Accessed: 9-11-25

import math

resistance = int(input("Enter the resistance: "))
voltage = int(input("Enter the voltage: "))

answer = voltage/resistance

print(f"Your current was {answer}")