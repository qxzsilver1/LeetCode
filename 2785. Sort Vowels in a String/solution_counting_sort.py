class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        count_dict = { k: 0 for k in vowels }

        for c in s:
            if c in count_dict:
                count_dict[c] += 1
        
        res = ''

        j = 0

        for i in range(len(s)):
            if s[i] not in count_dict:
                res += s[i]
            else:
                while count_dict[vowels[j]] == 0:
                    j += 1
                
                res += vowels[j]
                count_dict[vowels[j]] -= 1
        
        return res
