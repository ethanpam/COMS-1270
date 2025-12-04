# Ethan Pham    Lab-B    11-29-25
# Contains the whiteboard question top k frequency element from neetcode!

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

def test_topKFrequent():
    s = Solution()
    assert s.topKFrequent([1,2,2,3,3,3], 2) == [3,2]
    assert s.topKFrequent([7,7], 1) == [7]

def main():
    test_topKFrequent()

if __name__ == "__main__":
    main()