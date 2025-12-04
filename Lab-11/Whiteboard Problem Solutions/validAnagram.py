# Ethan Pham    Lab-B    11-29-25
# Contains the whiteboard question valid anagram from neetcode!

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
def test_isAnagram():
    s = Solution()
    assert s.isAnagram("racecar", "carrace") == True
    assert s.isAnagram("jar", "jam") == False

def main():
    test_isAnagram()

if __name__ == "__main__":
    main()