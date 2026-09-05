class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])

        first_half_cnt, second_half_cnt = 0, 0

        n = len(s)

        for i in range(n // 2):
            if s[i].lower() in vowel_set:
                first_half_cnt += 1
            
            if s[n - i - 1].lower() in vowel_set:
                second_half_cnt += 1
        
        return first_half_cnt == second_half_cnt
