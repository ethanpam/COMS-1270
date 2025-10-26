#Ethan Pham        10-9-25
#This finds the substring in string using 3 versions
def findSubStringV1(string, substr):
    return string.find(substr)

def findSubStringV2(string, substr):
    while True:
        if substr in string:
            return string.index(substr)
        else:
            return -1

def findSubStringV3(string, substr):
    for i in range(len(string) - len(substr)):
        check = string[i : i + int(len(substr))]
        if check == substr:
            return i
    if check != substr:
        return -1

def main():
    string = str(input("What is your string? "))
    substr = str(input("What is your substring? "))

    while True:
        version = int(input("What version do you want?\n[1][2][3]\n"))
        if version == 1:
            print(findSubStringV1(string, substr))
            return
        if version == 2:
            print(findSubStringV2(string, substr))
            return
        if version == 3:
            print(findSubStringV3(string, substr))
            return


if __name__ == "__main__":
    main()


#Version 1 find substring st "abcd xyz" checks if subs= "d x" is inside we can use .find() so st.find("subs") it will return -1
#Verison 2 similar to .find but st.index(subs = 3 this will crash so we need to apply condition whether substring is apart of string if it is than call it or else return -1 
#Verison 3 forloop str[0:3] or else check next string so [1:4] until i get a point w no window outside of string we can use for loop
