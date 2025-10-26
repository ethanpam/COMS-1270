#Ethan Pham        10-9-25
#This application builds a a triangle with each layer printed based on the relationship between int and width

'''
Prints a same number triangle base on the users input

@param num - The height of the triangle as well as layer
@return a triangle w integers as each layer
'''

def sameNumberTriangle(num):
    for i in range(num+1):
        for j in range(i):
            print(str(i), end="")
        print()

def main():
    num = int(input("what size is ur triangle? "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()