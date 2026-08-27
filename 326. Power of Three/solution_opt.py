class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_power = 3 ** 19
        
        return n > 0 and max_power % n == 0
