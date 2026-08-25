class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ascii_map = [0] * 128

        odd_counts = 0

        for i in range(len(s)):
            ascii_map[ord(s[i])] += 1

            if ascii_map[ord(s[i])] % 2 == 0:
                odd_counts -= 1
            else:
                odd_counts += 1
        
        return odd_counts <= 1
