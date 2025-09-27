#Ethan Pham            9-22-25        Lab B
#This code uses the random module to determine the random value between 'B' and 'C' given by the user's input, with that chosen random value being multipied by the previous value if the user to include an 'A' value higher than 1 (which A is the iteration of how many times a random number made using 'B' and 'C')

import random
r = random
def randomProduct(a,b,c):
    d = 1
    for i in range(a):
        d = d * r.randrange(b,c)
    return d

def main():
    A = int(input("Please enter value A: "))
    B =int(input("Please enter value B: "))
    C = int(input("Please enter value C: ")) + 1
    answer = randomProduct(A,B,C)
    print(f"Your answer was {answer}")

if __name__ == "__main__":
    main()