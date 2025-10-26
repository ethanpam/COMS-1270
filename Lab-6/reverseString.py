# Ethan Pham      10-9-25
# This application has five verisons that you can use to reverse a string

def reverseStringV1(string):
    return string[::-1]

def reverseStringV2(string):
    return ("".join(reversed(string)))

def reverseStringV3(string):
    chain = ""
    for i in range (len(string)-1, -1, -1):
        indexString = string[i]
        chain = chain + indexString
    return chain

def reverseStringV4(string):
    chain = ""
    for i in string:
        chain = i + chain
    return chain

def reverseStringV5(string):
    chain = ''
    i = len(string)
    while i-1>= 0:
        indexString = string[i-1]
        chain = chain + indexString
        i-=1
    return chain

def main():
    string = str(input("What is your string that you would want to reverse? "))
    while True:
        version = int(input("What version do you want?\n[1][2][3][4][5]\n"))
        if version == 1:
            print(reverseStringV1(string))
            break
        elif version == 2:
            print(reverseStringV2(string))
            break
        elif version == 3:
            print(reverseStringV3(string))
            break
        elif version == 4:
            print(reverseStringV4(string))
            break
        elif version == 5:
            print(reverseStringV5(string))
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()



#"Apple Cat" - len = 9
#version 1 str[0:5], str[6,] range(, 10). str[0:9;2]=ApeCt    str[8:1:-1] - ac aC ellpA.     str[:] == str         str[:-1] - reverse
#version 2 built in function .reversed().   var = reverse("Abc") - ['c', 'b', 'A'].  another func called '*'.join(var) which converts index back into string so it will be c*b*a
#verison 3 using for loop    yes = elppA.       for i in range(len(s)-1, -1, -1) goes 4,0 each time goes a step back chan = stri[i] yes+= char
#verison 4 similar to verison 3 but w/o range().   stri="Apple" len(stri)=5  for i in stri:    yes = i + yes (bc reverse i goes first before yes)  
#verison 5 uses while loop similar to verison 3 but u cant use for loop.      i = len(str).   while i >= 0:  res+=str[i] i+=i  
