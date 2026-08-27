class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = 0

        res = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cnt += 1
            else:
                res += (cnt + 1) * cnt // 2
                cnt = 0
        
        res += cnt * (cnt + 1) // 2

        return res
