class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet_counts = [0] * 26

        for i in range(len(s)):
            alphabet_counts[ord(s[i]) - ord('a')] += 1
            alphabet_counts[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if alphabet_counts[i] != 0:
                return False

        return True
