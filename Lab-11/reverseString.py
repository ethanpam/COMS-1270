# Ethan Pham    Lab-B    11-29-25
# This contains many functions that reverses a string

def reverseIterative(s):
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]

def test_reverseIterative():
    assert reverseIterative("abc") == "cba"
    assert reverseIterative("tacocat") == "tacocat"
    assert reverseIterative("pizza") == "azzip"

def test_reverseRecursive():
    assert reverseRecursive("abc") == "cba"
    assert reverseRecursive("tacocat") == "tacocat"
    assert reverseRecursive("pizza") == "azzip"

def main():
    s = str(input("Enter a string: "))
    
    test_reverseIterative()
    test_reverseRecursive()

    print(reverseIterative(s))
    print(reverseRecursive(s))

if __name__ == "__main__":
    main()
