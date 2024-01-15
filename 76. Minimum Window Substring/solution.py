class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '': return ''
        
        min_substring_interval = [-1, -1]
        min_substring_length = float('inf')

        m, n = len(s), len(t)

        t_dict = defaultdict(int)
        currently_matched_chars = 0

        for c in t:
            t_dict[c] += 1
        
        s_dict = dict.fromkeys(t_dict, 0)

        substring_chars_length = len(t_dict)
        
        l = 0

        for r in range(len(s)):
            c = s[r]

            if c in s_dict:
                s_dict[c] += 1
            else:
                continue

            if c in t_dict and t_dict[c] == s_dict[c]:
                currently_matched_chars += 1
            
            while currently_matched_chars == substring_chars_length:
                if (r - l + 1) < min_substring_length:
                    min_substring_length = r - l + 1
                    min_substring_interval = [l, r]
                
                if s[l] in s_dict:
                    s_dict[s[l]] -= 1

                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    currently_matched_chars -= 1
                
                l += 1
        
        l, r = min_substring_interval
        return s[l:r+1] if min_substring_length != float('inf') else ''
