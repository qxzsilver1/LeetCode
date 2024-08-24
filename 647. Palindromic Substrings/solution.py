class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_cnt = 0

        def count_palindromes(s, l, r):
            res = 0
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            return res

        for i in range(len(s)):
            l, r = i, i
            palindrome_cnt += count_palindromes(s, l, r)
            
            l, r = i, i+1
            palindrome_cnt += count_palindromes(s, l, r)
        
        return palindrome_cnt
