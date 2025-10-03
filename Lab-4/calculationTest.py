# Ethan Pham        9-25-25        Lab B
# This calculation uses imports from different calculations to create one massive calculation from different subjects such as 'myShapes', 'myPhysics', 'myOhms', and 'myFinances'
import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    setting = True
    while setting:
        path = input("Which module would you like to enter? \n[1]myShapes \n[2]myPhysics \n[3]myOhmsLaw \n[4]myFinances \n[q]uit\n")
        if path == "1":
            while setting:
                section = input("Which section would you like to calculate? \n[1]areaOfRectangle \n[2]rectanglePerimeter \n[3]areaOfCircle \n[4]circleCircumference \n[q]uit\n")
                if section == "1":
                    base = int(input("Enter the length of the base: "))
                    height = int(input("Enter the height of the rectangle: "))
                    answer = myShapes.areaOfRectangle(base, height)
                    setting = printAnswer(answer)
                if section == "2":
                    length = int(input("Enter the length of the rectangle: "))
                    width = int(input("Enter the width of the rectangle: "))
                    answer = myShapes.rectanglePerimeter(length, width)
                    setting = printAnswer(answer)
                if section == "3":
                    radius = int(input("Enter the radius of the circle: "))
                    answer = myShapes.areaOfCircle(radius)
                    setting = printAnswer(answer)
                if section == "4":
                    radius = int(input("Enter the radius of the base: "))
                    answer = myShapes.circleCircumference(radius)
                    setting = printAnswer(answer)
                if section == "q":
                    print("Goodbye!")
        if path == "2":
            while setting:
                section = input("Which section would you like to calculate? \n[1]distanceSpeedTime \n[2]velocityAccelerationTime \n[q]uit\n")
                if section == "1":
                    speed = int(input("Enter speed in meters per second: "))
                    time = int(input("Enter the time in seconds: "))
                    answer = myPhysics.distanceSpeedTime(speed, time)
                    setting = printAnswer(answer)
                if section == "2":
                    initial_v = int(input("Enter the initial velocity in meters per second: "))
                    acceleration = int(input("Enter the acceleration in meters per second squared: "))
                    time = int(input("Enter the time in seconds: "))
                    answer = myPhysics.velocityAccelerationTime(initial_v, acceleration, time)
                    setting = printAnswer(answer)
                if section == "q":
                    print("Goodbye!")
        if path == "3":
            while setting:
                section = input("Which section would you like to calculate? \n[1]calculateCurrent \n[2]calculateVoltage \n[3]calculateResistence \n[q]uit\n")
                if section == "1":
                    resistance = int(input("Enter the resistance: "))
                    voltage = int(input("Enter the voltage: "))
                    answer = myOhmsLaw.calculateCurrent(resistance, voltage)
                    setting = printAnswer(answer)
                if section == "2":
                    current = int(input("Enter the current: "))
                    resistance = int(input("Enter the resistence: "))
                    answer = myOhmsLaw.calculateVoltage(current, resistance)
                    setting = printAnswer(answer)
                if section == "3":
                    current = int(input("Enter the current: "))
                    voltage = int(input("Enter the voltage: "))
                    answer = myOhmsLaw.calculateResistence(voltage, current)
                    setting = printAnswer(answer)
                if section == "q":
                    print("Goodbye!")
                    setting = False
                    pass
        if path == "4":
            while setting:
                section = input("Which section would you like to calculate? \n[1]annualPercentageRate \n[2]compoundAmount \n[q]uit\n")
                if section == "1":
                    interest_c = int(input("Enter the interest charges: "))
                    fees = int(input("Enter the fees: "))
                    loan_a = int(input("Enter the loan amount: "))
                    days = int(input("Enter the days in term: "))
                    answer = myFinances.annualPercentageRate(interest_c, fees, loan_a, days)
                    setting = printAnswer(answer)
                    pass
                if section == "2":
                    principal = int(input("Enter the principal amount: "))
                    rate = int(input("Enter the interest rate (in percentage without the percentage sign): "))
                    number_c = int(input("Enter the number of times the interest compounds in a year: "))
                    time = int(input("Enter the time in years: "))
                    answer = myFinances.compoundAmount(principal, rate, number_c, time)
                    setting = printAnswer(answer)
                    pass
                if section == "q":
                    print("Goodbye!")
                    setting = False
        if path == "q":
            print("Goodbye!")
            return

def printAnswer(answer):
    print(f"Your answer was {answer}")
    return False

if __name__ == "__main__":
    main()