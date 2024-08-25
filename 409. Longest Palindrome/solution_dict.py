class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_dict = defaultdict(int)
        res = 0

        for c in s:
            cnt_dict[c] += 1

            if not cnt_dict[c] % 2:
                res += 2
        
        for cnt in cnt_dict.values():
            if cnt % 2:
                res += 1
                break
        
        return res
