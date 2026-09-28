class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        tmp = []

        for c in s:
            if c in vowels:
                tmp.append(c)
        
        tmp.sort()

        j = 0
        res = ''

        for i in range(len(s)):
            if s[i] in vowels:
                res += tmp[j]
                j += 1
            else:
                res += s[i]
        
        return res
