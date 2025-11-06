# Ethan Pham    Lab-B    11-3-25
# Counts the frequency of words in a book

def analyzeBook(filename):
    count = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():

                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')

                # ignore case
                word = word.lower()

                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def outputAnalysis(counts, title):
    title = title.replace(".txt", "_analysis.txt")
    keys = list(counts.keys())
    keys.sort()

    # save the word count analysis to a file

    with open(title, 'w') as file:
        for word in keys:
            file.write(word + " " + str(counts[word]))
            file.write('\n')

def main():
    filename = input("Enter the filename: ")
    countDict = (analyzeBook(filename))
    outputAnalysis(countDict, filename)

if __name__ == "__main__":
    main()