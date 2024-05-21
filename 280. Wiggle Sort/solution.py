class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            if (i % 2 and nums[i] < nums[i-1]) or (not i % 2 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
                continue
            
        return nums
