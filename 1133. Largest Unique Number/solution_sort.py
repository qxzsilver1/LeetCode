class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        nums.sort(reverse= True)

        i = 0

        while i < n:
            if i == n - 1 or nums[i] != nums[i+1]:
                return nums[i]
            
            while i < n - 1 and nums[i] == nums[i+1]:
                i += 1
            
            i += 1
        
        return -1
