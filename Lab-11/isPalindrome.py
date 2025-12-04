# Ethan Pham    Lab-B    11-29-25
# Contains iterative and recursive forms of palindrome

def isPalindromeIterative(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])

def test_isPalindromeIterative():
    assert isPalindromeIterative("tacocat") == True
    assert isPalindromeIterative("racecar") == True
    assert isPalindromeIterative("pizza") == False

def test_isPalindromeRecursive():
    assert isPalindromeRecursive("tacocat") == True
    assert isPalindromeRecursive("racecar") == True
    assert isPalindromeRecursive("pizza") == False

def main():
    s = str(input("Enter a string: "))
    
    test_isPalindromeIterative()
    test_isPalindromeRecursive()

    print(isPalindromeIterative(s))
    print(isPalindromeRecursive(s))

if __name__ == "__main__":
    main()
