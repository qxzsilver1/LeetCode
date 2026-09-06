class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = 0

        def twoSumSmaller(nums, start_idx, target):
            res = 0

            l, r = start_idx, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            
            return res

        for i in range(len(nums) - 2):
            res += twoSumSmaller(nums, i + 1, target - nums[i])
        
        return res
