class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict, t_dict = {}, {}
        
        for i, c in enumerate(s):
            s_dict[c] = i
        
        for i, c in enumerate(t):
            t_dict[c] = i
        
        res = 0

        for k in s_dict:
            res += abs(s_dict[k] - t_dict[k])
        
        return res
