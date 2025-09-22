import random
r = random
def randomProduct(a,b,c):
    d = 1
    for i in range(a):
        d = d * r.randrange(b,c)
    return d

def main():
    A = int(input("Please enter value A: "))
    B =int(input("Please enter value B: "))
    C = int(input("Please enter value C: ")) + 1
    answer = randomProduct(A,B,C)
    print(f"Your answer was {answer}")

if __name__ == "__main__":
    main()