#Ethan Pham     10-9-25
#This function checks whether a string is palindrom or not
#noon is palindrom bc noon reverse is noon so is madam 

import reverseString

def pallindromeCheckV1(palindromeString):
    reverse = reverseString.reverseStringV1(palindromeString)
    if reverse == palindromeString:
        return True
    else:
        return False

def paliindromeCheckV2(palindromeString):
    start = 0
    end = len(palindromeString)-1
    while start <= end:
        if palindromeString[start] != palindromeString[end]:
            return False
        start += 1
        end -= 1
    return True

def main():
    palindromeString = input("What is your palindrome? ")
    while True:
        version = int(input("What version do you want?\n[1][2]\n"))
        if version == 1:
            value = pallindromeCheckV1(palindromeString)
            break
        if version == 2:
            value = paliindromeCheckV2(palindromeString)
            break
        else:
            print("Invalid choice")
    print("It is a palindrome!" if value else "It is not a palindrome!")

if __name__ == "__main__":
    main()
