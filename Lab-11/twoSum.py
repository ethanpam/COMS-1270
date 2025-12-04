# Ethan Pham    Lab-B    11-29-25
# This file has four functions: two finding one pair that matches a target and two finding all pairs matching that target

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def twoSumLoopsAll(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i,j])
    return result

def twoSumDict(nums, target):
    num_dict = {} 
    for i, num in enumerate(nums):
        needed = target - num #variables: i, num    enumerate() - built in python function that loops through a list and finds the element's index and returns pairs (index, value) (i,num)
        if needed in num_dict:
            return [num_dict[needed], i]
        num_dict[num] = i

def twoSumDictAll(nums: list[int], target: int) -> list[int]: 
    seen = {} 
    results = [] 
    for i, num in enumerate(nums): 
        needed = target - num 
        if needed in seen: 
            results.append([seen[needed], i]) 
        seen[num] = i 
    return results

def test_SumLoops():
    assert twoSumLoops([2,7,11,15],9) == [0,1]
    assert twoSumLoops([3,2,4], 6) == [1,2]
    assert twoSumLoops([3,3], 6) == [0,1]

def test_SumDict():
    assert twoSumDict([2,7,11,15],9) == [0,1]
    assert twoSumDict([3,2,4], 6) == [1,2]
    assert twoSumDict([3,3], 6) == [0,1]

def main():
    nums = [2,7,11,15,7,-2,9]
    target = 9

    test_SumLoops()
    test_SumDict()
    
    print(twoSumLoops(nums,target))
    print(twoSumDict(nums, target))

    print(twoSumLoopsAll(nums, target))
    print(twoSumDictAll(nums, target))

if __name__ == "__main__":
    main()