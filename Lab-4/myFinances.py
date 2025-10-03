# Ethan Pham        9-25-25        Lab B
# This application stores functions/calculations
def annualPercentageRate(i, f, l, d):
    # Citation - URL: https://www.investopedia.com/terms/a/apr.asp
    # Citation - Author: Jason Fernando
    # Citation - Date Published: 10-23-25
    # Citation - Date Accessed: 9-11-25
    return (((i + f)/l)/d)*100


def compoundAmount(p, r, c, t):
    # Citation - URL: https://www.investopedia.com/terms/a/accruedinterest.asp
    # Citation - Author: Will Kenton
    # Citation - Date Published: 9-8-2023
    # Citation - Date Accessed: 9-11-25
    return p * (1 +(r/100)/c)**(c*t)