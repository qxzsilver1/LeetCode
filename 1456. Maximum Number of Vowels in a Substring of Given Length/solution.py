class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        curr_sum = 0
        res = 0

        l = 0
        
        for i in range(l, k):
            if s[i] in vowel_set:
                curr_sum += 1
        
        res = curr_sum

        for r in range(k, len(s)):
            if s[r] in vowel_set:
                curr_sum += 1

            if s[l] in vowel_set and s[l]:
                curr_sum -= 1
            
            res = max(res, curr_sum)
            
            l += 1

        return res
