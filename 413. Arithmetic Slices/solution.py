class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = [0]

        def slices(nums, i):
            if i < 2:
                return 0
            
            ap = 0

            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                ap = slices(nums, i - 1) + 1
                res[0] += ap
            else:
                slices(nums, i - 1)

            return ap
        
        slices(nums, len(nums) - 1)

        return res[0]
