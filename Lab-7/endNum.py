#Ethan Pham         10-24-25
#Puts desire number into end of list

def endNum(intList, num):
    numList = []
    for i in intList:
        if i == num:
            numList.append(i)
            intList.remove(i)
        else:
            continue
    return (intList + numList)

def main():
    intList = []
    while True:
        n = input("Enter number (* to stop): ")
        if n == "*":
            break
        else:
            intList.append(int(n))
    num = int(input("What is num?: "))   
    print(endNum(intList, num))


if __name__ == "__main__":
    main()
