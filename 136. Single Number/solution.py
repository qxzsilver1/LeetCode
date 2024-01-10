class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s = s ^ n
        
        return s
