class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        char_diff_cnt = 0
        diff_indices = []

        for i in range(n):
            if s1[i] != s2[i]:
                char_diff_cnt += 1
                diff_indices.append(i)
            else:
                continue
            
            if char_diff_cnt > 2:
                return False
        
        if char_diff_cnt % 2 == 0:
            return char_diff_cnt == 0 or s1[diff_indices[0]] == s2[diff_indices[1]] and s1[diff_indices[1]] == s2[diff_indices[0]]
        else:
            return False

        
