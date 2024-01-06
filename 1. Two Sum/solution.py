class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        lookup = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if (complement in lookup):
                return [lookup[complement], i]
            else:
                lookup[nums[i]] = i
        return None
