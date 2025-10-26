#Ethan Pham                          10/7/25
#This application creates a pyramid out of numbers

def numberPyramid(num):
    for i in range(1, num + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line.center(num * 3))

def main():
    num = int(input("What size is your triangle? "))
    numberPyramid(num)


if __name__ == "__main__":
    main()