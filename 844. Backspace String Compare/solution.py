class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextValidChar(st, idx):
            cnt_backspace = 0
            
            while idx >= 0:
                if cnt_backspace == 0 and st[idx] != '#':
                    break
                elif st[idx] == '#':
                    cnt_backspace += 1
                else:
                    cnt_backspace -= 1
                idx -= 1
            
            return idx
        
        idx_s, idx_t = len(s) - 1, len(t) - 1

        while idx_s >= 0 or idx_t >= 0:
            idx_s = nextValidChar(s, idx_s)
            idx_t = nextValidChar(t, idx_t)

            char_s = s[idx_s] if idx_s >= 0 else ''
            char_t = t[idx_t] if idx_t >= 0 else ''

            if char_s != char_t:
                return False
            
            idx_s -= 1
            idx_t -= 1
        
        return True
