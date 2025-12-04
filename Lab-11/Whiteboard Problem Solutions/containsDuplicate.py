# Ethan Pham    Lab-B    11-29-25
# Contains the whiteboard question contains duplicate from neetcode!

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False

def test_hasDuplicate():
    s = Solution()
    assert s.hasDuplicate([1,2,3,4]) == False
    assert s.hasDuplicate([1,2,3,1]) == True

def main():
    test_hasDuplicate()

if __name__ == "__main__":
    main()