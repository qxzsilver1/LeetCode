class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for num in range(2, n):
            isPrime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    isPrime = False
                    break
            if isPrime:
                res += 1
        return res
