class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindrome_lengths = {} # mapping of bitmask -> length of palindrome

        for mask in range(1, 1 << n): # 2^n range for bitshift
            subsequence = ''

            for i in range(n):
                if mask & (1 << i):
                    subsequence += s[i] # can also be s[n - i - 1], but result is the same
                
            if subsequence == subsequence[::-1]:
                palindrome_lengths[mask] = len(subsequence)
        
        res = 0

        for m1 in palindrome_lengths:
            for m2 in palindrome_lengths:
                if m1 & m2 == 0:
                    res = max(res, palindrome_lengths[m1] * palindrome_lengths[m2])
        
        return res

