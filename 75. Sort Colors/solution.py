class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_dict = {0: 0, 1: 0, 2: 0}

        for n in nums:
            color_dict[n] += 1
        
        for i in range(len(nums)):
            if color_dict[0] > 0:
                nums[i] = 0
                color_dict[0] -= 1
            elif color_dict[1] > 0:
                nums[i] = 1
                color_dict[1] -= 1
            else:
                nums[i] = 2
                color_dict[2] -= 1
        
        return nums

        
