class Solution:
    def fib(self, n: int) -> int:
        
        def fast_double(n):
            if n == 0:
                return (0, 1)
            
            f_k, f_k_plus_1 = fast_double(n // 2)
            f_2k = f_k * (2 * f_k_plus_1 - f_k)
            f_2k_plus_1 = f_k_plus_1 ** 2 + f_k ** 2

            if n % 2 == 0:
                return (f_2k, f_2k_plus_1)
            else:
                return (f_2k_plus_1, f_2k + f_2k_plus_1)
        
        return fast_double(n)[0]
