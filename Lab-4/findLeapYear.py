# Ethan Pham        9-27-25        Lab B
# This application can tell you the leap year of any year!
def findLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Please enter a year: "))
    answer = findLeapYear(year)
    if answer == True:
        print("Your year is a leap year!")
    elif answer == False:
        print("Your year is not a leap year!")

if __name__ == "__main__":
    main()