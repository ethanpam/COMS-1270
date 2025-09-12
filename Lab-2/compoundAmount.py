#Ethan Pham        9-11-25
#Lab 2 - This code is calculated with the amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out

# Citation - URL: https://www.investopedia.com/terms/a/accruedinterest.asp
# Citation - Author: Will Kenton
# Citation - Date Published: 9-8-2023
# Citation - Date Accessed: 9-11-25

import math

principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate (in percentage without the percentage sign): "))
number_c = int(input("Enter the number of times the interest compounds in a year: "))
time = int(input("Enter the time in years: "))

answer = principal * (1 +(rate/100)/number_c)**(number_c*time)

print(f"Your accrued amount was {answer}")