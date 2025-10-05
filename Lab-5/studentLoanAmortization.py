#Ethan Pham           10-4-25
#This helps you plan out your student loan!
#Citation Source: https://www.investopedia.com/terms/a/amortization.asp
#Citation Author: Christian Allred
#Citation Access: 10-4-25

#Amortization - An accounting technique used to periodically lower the book value of a loan or an intangible asset over a set period of time
#wants input of principal, yearlyInterestRate, numberOfYears
#function takes input of these ^
#studentLoanAmortization prints out columns: Period Due, Computed Interest, Principal Due, Principal Balance

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    i = yearlyInterestRate/12
    n = numberOfYears * 12
    principalAmountRemaining = principal
    if yearlyInterestRate == 0:
        monthlyPayment = principal / n #0/12 does not work so i is not needed  principal * (dne * (1 + dne)**n)
    else:
        monthlyPayment = principal * (i * (1 + i)**n) / ((1 + i)**n - 1)
    for k in range(n): #i starts 0
        computedInterest = principalAmountRemaining * i
        principalDue = monthlyPayment - computedInterest
        principalAmountRemaining = principalAmountRemaining - principalDue
        print(f"{k+1:<10}{round(monthlyPayment,2):<21}{round(computedInterest,2):<21}{round(principalDue,2):<17}{round(principalAmountRemaining,2)}")

def main():
    principal = float(input("Please your principal: "))
    yearlyInterestRate = float(input("Please enter your yearly interest rate in decimal values: "))
    while True:
        numberOfYears = int(input("Please enter the numbers of year in integer values: "))
        if numberOfYears != 0:
            break
        else:
            print("Number of years cannot be 0!")
    print(f"{'Period':<10}{'Total Payment Due' :<21}{'Computed Interest' :<21}{'Principal Due' :<17}{'Principal Balance'}") #Based on length of word and left aligned '<' left, '^' center, '>' right {pro tip: its like writing a word doc} https://www.youtube.com/shorts/KmQgF1D4HOs
    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)

if __name__ == "__main__":
    main()


#total payment due 
# P x (i(1+i)^n)/((1+i)^n-1)

#computed interest
#bk-1*i

#principaldue 
#totalpaymentdue - interest_k

#principal balance
#b_k-1 - principaldue_k

#p = original principal (loan amount)
#i = (annual interest rate) (monthly rate)
#n = total number of payments = years x 12
#B_k-1 = balance before payment 
#k = 1-12
