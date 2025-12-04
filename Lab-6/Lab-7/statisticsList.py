#Ethan Pham         10-24-25
#Finds the mean and median of a random list
import random

def generateInput() -> list[int]:
    randoList = []
    for i in range(random.randint(200,500)):
        j = random.randint(1,2000)
        randoList.append(j)
    return randoList

def findMean(randoList: list[int]) -> float:
    """
    Citation URL: https://www.techtarget.com/searchdatacenter/definition/statistical-mean-median-mode-and-range
    Author: TechTarget Contributor
    Published: 10/9/25
    Date Accessed: 10/28/25
    """
    count = 0
    for i in range(len(randoList)):
        count += randoList[i]
    return (count/len(randoList))

def findMedian(randoList: list[int]) -> float:
    """
    Citation URL: https://www.techtarget.com/searchdatacenter/definition/statistical-mean-median-mode-and-range
    Author: TechTarget Contributor
    Published: 10/9/25
    Date Accessed: 10/28/25
    """
    randoList.sort()
    if (len(randoList)%2) == 0:
        return (randoList[((len(randoList)//2)-1)] + randoList[len(randoList)//2])/2
    else:
        return randoList[len(randoList)//2]

def main():
    randoList = generateInput()
    mean = round(findMean(randoList), 2)
    median = round(findMedian(randoList), 2)
    print("Mean = {} Median: {}".format(mean, median))

if __name__ == "__main__":
    main()

