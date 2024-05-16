class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_set = set()

        if len(nums) == 2:
            return False
        
        curr_sum = nums[0] + nums[1]
        sum_set.add(curr_sum)

        for i in range(1, len(nums) - 1):
            curr_sum -= nums[i-1]
            curr_sum += nums[i+1]

            if curr_sum in sum_set:
                return True
            
            sum_set.add(curr_sum)
        
        return False
