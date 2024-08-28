class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted([j for i, j in enumerate(nums) if not i % 2])
        odds = sorted([j for i, j in enumerate(nums) if i % 2], reverse=True)

        res = []

        for i in range(len(odds)):
            res.append(evens[i])
            res.append(odds[i])
        
        if len(evens) > len(odds):
            res.append(evens[-1])
        
        return res
