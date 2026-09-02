class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        prefix_str = ''
        suffix_str = ''

        for i in range(n // 2):
            j = n - i - 1

            min_char = min(s[i], s[j])
            prefix_str += min_char
            suffix_str += min_char
        
        if n % 2 == 1:
            prefix_str += s[n // 2]
        
        return prefix_str + suffix_str[::-1]
