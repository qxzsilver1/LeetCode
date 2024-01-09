class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output, count = 0, 0

        for n in nums:
            if count == 0:
                output = n
            
            count += 1 if n == output else -1
        
        return output
