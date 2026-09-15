class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        res = 0
        start = 0

        def checkPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        for r in range(k - 1, n):
            l = r - k + 1

            if l >= start and checkPalindrome(l, r):
                res += 1
                start = r + 1
                continue
            
            l = r - k

            if l >= start and checkPalindrome(l, r):
                res += 1
                start = r + 1
        
        return res
