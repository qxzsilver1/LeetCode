class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = inf

        for l in range(n):
            tmp = 0

            for r in range(l, n):
                tmp |= nums[r]

                if tmp >= k:
                    res = min(res, r - l + 1)
                    break
        
        return res if res != inf else -1
