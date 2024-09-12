class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n;
        
        arr = [-1] * (n + 1)
        arr[0], arr[1] = 0, 1

        for i in range(2, n+1):
            arr[i] = arr[i - 1] + arr[i - 2]
        
        return arr[n]
