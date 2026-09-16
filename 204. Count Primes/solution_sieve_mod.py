class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        sieve = [False] * n
        sieve[0] = sieve[1] = True
        res = 0
        
        for num in range(2, int(math.sqrt(n)) + 1):
                for i in range(num * num, n, num):
                    sieve[i] = True
        
        for is_not_prime in sieve:
            if not is_not_prime:
                res += 1
        
        return res
