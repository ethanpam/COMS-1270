# Ethan Pham    Lab-B    11-3-25
# This removes non ASCII in a text

def readFile(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content

def removeNonASCII(text):
    clean = ''
    for i in text:
        if ord(i) >= 0 and ord(i) <= 127:
            clean = clean + i
    return clean

def cleanNewFile(filename, clean):
    filename = filename.replace(".txt", "_clean.txt")
    with open(filename, 'w') as file:
        file.write(clean)


def main():
    filename = input("Enter the filename: ")
    text = readFile(filename)
    clean = (removeNonASCII(text))
    cleanNewFile(filename, clean)

if __name__ == "__main__":
    main()