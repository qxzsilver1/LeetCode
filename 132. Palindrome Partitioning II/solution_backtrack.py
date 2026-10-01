class Solution:
    def minCut(self, s: str) -> int:

        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            return True
        
        def findMinimumCut(s: str, start: int, end: int, min_cut: int) -> int:
            if start == end or isPalindrome(s, start, end):
                return 0
            
            for i in range(start, end + 1):
                if isPalindrome(s, start, i):
                    min_cut = min(min_cut, 1 + findMinimumCut(s, i + 1, end, min_cut))
            
            return min_cut
        
        return findMinimumCut(s, 0, len(s) - 1, len(s) - 1)
