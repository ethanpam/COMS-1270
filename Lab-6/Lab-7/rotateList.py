#Ethan Pham         10-24-25
#Rotates list based on the rotation number

def rotateList(intList, rot):
    n = len(intList)
    if rot == 0:
        return intList
    rot = rot % n
    if rot > 0:
        return intList[-rot:] + intList[:-rot]
    elif rot < 0:
        return intList[-rot:] + intList[:-rot]
    else:
        return intList

def main():
    intList = []
    while True:
        n = input("What is your number?(* to stop): ")
        if n == "*":
            break
        else:
            intList.append(int(n))
    rot = int(input("What is your rotation number? "))
    print(rotateList(intList, rot))


if __name__ == "__main__":
    main()