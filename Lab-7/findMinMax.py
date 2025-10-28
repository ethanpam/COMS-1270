def findMin(int_numbers):
    min = int_numbers[0]
    for i in int_numbers:
        if min > i:
            min = i
    return min

def findMax(int_numbers):
    max = 0
    for i in int_numbers:
        if max < i:
            max = i
    return max

def main():
    str_numbers = []
    int_numbers = []
    while True:
        number = str(input("Input value (* to stop): "))
        if number == "*":
            break
        else:
            str_numbers.append(number)
    for i in str_numbers:
        int_numbers.append(int(i))
    print(f"Your lowest number was: {findMin(int_numbers)}")
    print(f"Your highest number was: {findMax(int_numbers)}")

if __name__ == "__main__":
    main()