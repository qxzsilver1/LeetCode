class Solution:
    def minCut(self, s: str) -> int:
        memo_cuts = [[None] * len(s) for _ in range(len(s))]
        memo_palindrome = [[None] * len(s) for _ in range(len(s))]

        def isPalindrome(s: str, start: int, end: int) -> bool:
            if start >= end:
                return True
            
            if memo_palindrome[start][end] != None:
                return memo_palindrome[start][end]
            
            memo_palindrome[start][end] = s[start] == s[end] and isPalindrome(s, start + 1, end - 1)
            
            return memo_palindrome[start][end]
        
        def findMinimumCut(s: str, start: int, end: int, min_cut: int) -> int:
            if start == end or isPalindrome(s, start, end):
                return 0
            
            if memo_cuts[start][end] != None:
                return memo_cuts[start][end]
            
            for i in range(start, end + 1):
                if isPalindrome(s, start, i):
                    min_cut = min(min_cut, 1 + findMinimumCut(s, i + 1, end, min_cut))
            
            memo_cuts[start][end] = min_cut
            
            return memo_cuts[start][end]
        
        return findMinimumCut(s, 0, len(s) - 1, len(s) - 1)
