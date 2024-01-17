class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = [-1] * 128
        t_to_s = [-1] * 128
        n = len(s)

        for i in range(n):
            s_index = ord(s[i])
            t_index = ord(t[i])

            if s_to_t[s_index] == -1 and t_to_s[t_index] == -1:
                s_to_t[s_index] = t_index
                t_to_s[t_index] = s_index
            
            if s_to_t[s_index] != t_index or t_to_s[t_index] != s_index:
                return False
        
        return True
