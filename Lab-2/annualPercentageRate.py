#Ethan Pham        9-11-25
#Lab 2 - This code is calculated by multiplying the periodic interest rates by the numbers of period in a year

# Citation - URL: https://www.investopedia.com/terms/a/apr.asp
# Citation - Author: Jason Fernando
# Citation - Date Published: 10-23-25
# Citation - Date Accessed: 9-11-25

import math

interest_c = int(input("Enter the interest charges: "))
fees = int(input("Enter the fees: "))
loan_a = int(input("Enter the loan amount: "))
days = int(input("Enter the days in term: "))

answer = (((interest_c + fees)/loan_a)/days)*100

print(f"Your apr was {answer}")