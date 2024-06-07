class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowel_set = set(['a', 'e', 'i', 'o', 'u'])

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() in vowel_set and s[r].lower() in vowel_set:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            
            if s[l].lower() not in vowel_set:
                l += 1
            
            if s[r].lower() not in vowel_set:
                r -= 1
        
        return ''.join(s)
