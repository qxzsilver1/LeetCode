class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odds, evens = 0, 0

        for n in nums:
            odds ^= (n & ~evens)
            evens ^= (n & ~odds)
        
        return odds
