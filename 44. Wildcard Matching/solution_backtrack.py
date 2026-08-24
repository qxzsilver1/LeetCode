class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_len, pattern_len = len(s), len(p)

        s_idx, p_idx = 0, 0
        star_idx = -1
        s_tmp_idx = -1

        while s_idx < str_len:
            if p_idx < pattern_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            
            elif p_idx < pattern_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            
            elif star_idx == -1:
                return False
            
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        return all(p[i] == '*' for i in range(p_idx, pattern_len))
