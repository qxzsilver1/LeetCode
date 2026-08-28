class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        if s_len > t_len:
            s, t = t, s
            s_len, t_len = t_len, s_len
        
        if t_len - s_len > 1:
            return False
        
        for i in range(s_len):
            if s[i] != t[i]:
                if s_len == t_len:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        
        return s_len + 1 == t_len
