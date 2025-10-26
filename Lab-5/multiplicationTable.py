#Ethan Pham             10-4-25
#This shows a outputs a multiplication table based on your lowest number and highest number

'''
Prints a multiplication table by using a nested loop with the range of two integers

@param lowNum - Integer value lower than highNum
@param highNum - Integer value higher than lowNum
@return - prints out Multiplication Table of lowNum-highNum
'''
def multipilicationTable(lowNum, highNum):
    for i in range(lowNum,highNum):
        for j in range(lowNum, highNum):
            print(str(i * j).rjust(4), '', end='')
        print()

def main():
    while True:
        lowNum = int(input("Please input the lowest number: "))
        highNum = int(input("Please input the highest number: ")) + 1
        if lowNum > highNum:
            print("Your 'lower' number is bigger than the 'higher' number")
        else:
            break
    multipilicationTable(lowNum,highNum)

if __name__ == "__main__":
    main()