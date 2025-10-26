#Ethan Pham.            10-6-25
#This program creates a right triangle based on your inputs

def starRightTriangle(num):
    for i in range(num+1):
        print("*" * i)

def main():
    num = int(input("what size is ur triangle? "))
    starRightTriangle(num)


if __name__ == "__main__":
    main()