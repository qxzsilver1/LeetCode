class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        for r in reversed(range(len(s))):
            if isPalindrome(s, 0, r):
                suffix = s[r + 1:]
                return suffix[::-1] + s
        
        return ''
