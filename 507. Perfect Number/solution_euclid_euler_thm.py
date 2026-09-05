class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        def evenPerfectNumber(p):
            return (1 << (p - 1)) * ((1 << p) - 1)
        
        mersenne_primes = [2, 3, 5, 7, 13, 17, 19, 31]

        for p in mersenne_primes:
            if evenPerfectNumber(p) == num:
                return True
        
        return False
