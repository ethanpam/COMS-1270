#Ethan Pham            9-23-25        Lab B
#This code takes inputs of an x value and iteration value to determine the approximation of a square root by using math equations and 'for loops' 
# Citation - https://www.cuemath.com/algebra/square-root-of-2/
# Citation - Author: Cuemath
# Citation - Date Accessed: 9-23-25

import math

def sqrtIter(x, itera):
    y = (x + 1)/2
    
    for i in range(itera):
        y = ((x/y)+y)/2
    return y

def main():
    x = int(input("Please insert an X value: "))
    itera = int(input("Please insert how many iterations you want: "))
    answer = sqrtIter(x, itera)
    print("The answer is:", answer)

if __name__ == "__main__":
    main()