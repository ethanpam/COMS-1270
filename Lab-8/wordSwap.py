# Ethan Pham    Lab-B    11-3-25
# Switches words around

import random

def wordSwap(sentence):
    wordSwap = {}
    words = sentence.strip().split()
    for char in words:
        wordSwap[char] = random.choice(words)
    return ' '.join(wordSwap[i] for i in words)

def main():
    sentence = str(input("Write a sentence: "))
    print(wordSwap(sentence))

if __name__ == "__main__":
    main()