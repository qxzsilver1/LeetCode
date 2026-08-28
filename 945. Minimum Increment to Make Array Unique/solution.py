class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnts = Counter(nums)

        res = 0

        for i in range(len(nums) + max(nums)):
            if cnts[i] > 1:
                extra = cnts[i] - 1
                cnts[i + 1] += extra
                res += extra

        return res
