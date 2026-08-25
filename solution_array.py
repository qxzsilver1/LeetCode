class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ascii_map = [0] * 128

        for c in s:
            ascii_map[ord(c)] += 1
        
        odd_counts = 0

        for c in ascii_map:
            if c % 2:
                odd_counts += 1
        
        return odd_counts <= 1
