def endNum(intList, num):
    numList = []
    for i in intList:
        intList.append(int(i))
        intList.remove(i)
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
        n = str(input("Enter integer (* to stop): "))
        if n == "*":
            break
        else:
            intList.append(n)
    num = int(input("What is num?: "))   
    print(endNum(intList, num))


if __name__ == "__main__":
    main()
"""
NOT FINISHED
"""