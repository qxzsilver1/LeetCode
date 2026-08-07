class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = []

        for a, b in pairwise(nums):
            res.extend(range(a+1, b))
        
        return res
