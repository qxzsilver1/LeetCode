class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def sumOfSquares(n):
            output = 0

            while n:
                output += (n % 10) ** 2
                n //= 10
            
            return output
        
        slow = fast = n
        slow = sumOfSquares(slow)
        fast = sumOfSquares(fast)
        fast = sumOfSquares(fast)

        while slow != fast:
            if fast == 1:
                return True
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        
        if slow == 1:
            return True
        else:
            return False
