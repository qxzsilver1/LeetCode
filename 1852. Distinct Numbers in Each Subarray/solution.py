class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        counts = {}

        res = []

        for i, v in enumerate(nums):
            counts[v] = counts.get(v, 0) + 1

            if i >= k:
                old = nums[i - k]
                counts[old] -= 1

                if counts[old] == 0:
                    del counts[old]
            
            if i >= k - 1:
                res.append(len(counts))
        
        return res
