class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        curr_len = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                curr_len += 1
                res = max(res, curr_len)
            else:
                curr_len = 1
        
        return res
