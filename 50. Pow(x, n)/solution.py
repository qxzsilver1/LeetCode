class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            output = helper(x, n // 2)
            output = output * output
            return x * output if n % 2 else output
        
        output = helper(x, abs(n))
        
        return output if n >= 0 else 1 / output
