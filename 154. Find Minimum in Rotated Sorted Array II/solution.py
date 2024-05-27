class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[0]

        while l <= r:

            m = l + (r-l) // 2

            output = min(output, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                r -= 1
        
        return output
