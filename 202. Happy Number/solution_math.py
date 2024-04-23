class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        visited = set()

        def sumOfSquares(n):
            output = 0

            while n:
                output += (n % 10) ** 2
                n //= 10
            
            return output

        while n not in visited:
            if n == 1:
                return True
            
            visited.add(n)
            n = sumOfSquares(n)
        
        return False
