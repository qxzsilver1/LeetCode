class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        divisor = 1

        while x >= 10 * divisor:
            divisor *= 10
        
        while x:
            right = x % 10
            left = x // divisor

            if left != right:
                return False
            
            x = (x % divisor) // 10
            divisor //= 100
        
        return True
