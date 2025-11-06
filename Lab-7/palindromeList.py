# Ethan Pham         10-24-25
# Palindrome a list

def palindromeList(palList):
    j = 0
    for i in palList:
        if i == palList[(len(palList)-1)-j]:
            j += 1
            continue
        else:
            return False
    return True

def main():
    palList = []
    while True:
        pal = str(input("Enter your string (* to stop): "))
        if pal == "*":
            break
        else:
            palList.append(pal)
    print(f"Your answer was: {palindromeList(palList)}")

if __name__ == "__main__":
    main()