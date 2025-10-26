#Ethan Pham       10-8-25
#This code creates diamond out of numbers!

def numberDiamond(num):
    for i in range(1, num + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line.center(num * 4))
    for i in range(num - 1, 0, -1):
        line = ' '.join(str(j+1) for j in range(i))
        print(line.center(num * 4))

def main():
    num = int(input("What size is your triangle? "))
    numberDiamond(num)

if __name__ == "__main__":
    main()