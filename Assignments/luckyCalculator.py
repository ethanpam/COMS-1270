#Ethan Tan Phuc Pham           9-22-2025
#Assignment 2
#This digital calculator can calculate your inputs of A & B into 7 different operations, including '+' '-' '*' '/' '//' '%' '**'
#Not only that but you can also generate your lucky number through the range you choose!
#Have fun! :)

import random

print("\nLucky Calculator!\n\nBy: Ethan Pham\n[COM S 1270 Section 4]")

while True:
    selection = str(input("\nWhat would you like to Do?\n\n[c]alculator, [l]ucky number, [q]uit: "))
    if selection == "c":
        while True:
            calculations = input("Please choose a Calculation [+] [-] [*] [/] [//] [%] [**]:  ")
            if calculations == "+" or calculations == "-" or calculations == "*" or calculations == "/"or calculations == "//" or calculations == "%" or calculations == "**":
                break
            print("ERROR: Please enter a valid operation")
        while True:
            a = int(input("Please enter integer A: "))
            while True:
                b = int(input("Please enter integer B: "))
                if calculations == "/" or calculations == "//" or calculations == "%":
                    if b != int(0):
                        break
                    else:
                        print("ERROR: division by 0 does not work")
                else:
                    break
            break
        if calculations == "+":
            c = a + b
        elif calculations == "-":
            c = a - b
        elif calculations == "*":
            c = a * b
        elif calculations == "/":
            c = a/b
        elif calculations == "//":
            c = a//b
        elif calculations == "%":
            c = a%b
        elif calculations == "**":
            c = a**b
        print(f"With {a} {calculations} {b} your final answer was {c}")
        break
    if selection == "l":
        while True:
            a = int(input("Please enter integer A: "))
            b = int(input("Please enter integer B: ")) + 1
            if a<b:
                break
            else:
                print("ERROR: A is greater than B")
        c = random.randrange(a,b)
        print(f"Your lucky number was {c}")
        break
    if selection == "q":
        print("Goodbye!")
        break



