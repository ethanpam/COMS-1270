# Ethan Pham    Lab-B    11-29-25
# Contains modulus and dictionary version of fizz buzz

def fizzBuzzModulus(n):
    fizzBuzz = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzz.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzz.append("Fizz")
        elif i % 5 == 0:
            fizzBuzz.append("Buzz")
        elif i % 7 == 0:
            fizzBuzz.append("Bazz")
        else:
            fizzBuzz.append(f"{i}")
    return fizzBuzz

def fizzBuzzDict(n):
    rules = {
        3: "Fizz",
        5: "Buzz",
        7: "Bazz"
    }
    result = []
    for i in range(1, n + 1):
        output = ""
        for key in rules:
            if i % key == 0:
                output += rules[key]
        if output == "":
            result.append(str(i))
        else:
            result.append(output)
    return result

def test_fizzBuzzModulus():
    assert fizzBuzzModulus(3) == ["1","2","Fizz"]
    assert fizzBuzzModulus(5) == ["1","2","Fizz","4","Buzz"]
    assert fizzBuzzModulus(15) == ["1","2","Fizz","4","Buzz","Fizz","Bazz","8","Fizz","Buzz","11","Fizz","13","Bazz","FizzBuzz"]

def test_fizzBuzzDict():
    assert fizzBuzzDict(3) == ["1","2","Fizz"]
    assert fizzBuzzDict(5) == ["1","2","Fizz","4","Buzz"]
    assert fizzBuzzDict(15) == ["1","2","Fizz","4","Buzz","Fizz","Bazz","8","Fizz","Buzz","11","Fizz","13","Bazz","FizzBuzz"]

def main():
    n = int(input("Please enter a number: "))
    
    test_fizzBuzzModulus()
    test_fizzBuzzDict()

    print(fizzBuzzModulus(n))
    print(fizzBuzzDict(n))

if __name__ == "__main__":
    main()