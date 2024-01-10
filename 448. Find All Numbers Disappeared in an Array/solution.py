class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1*abs(nums[i])
        
        output = []

        for i, n in enumerate(nums):
            if n > 0:
                output.append(i+1)
        
        return output
