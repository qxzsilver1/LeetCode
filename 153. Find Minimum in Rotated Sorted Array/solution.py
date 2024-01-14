class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                output = min(output, nums[l])
                break

            m = l + (r-l) // 2

            output = min(output, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return output
