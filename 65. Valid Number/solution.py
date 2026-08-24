class Solution:
    def isNumber(self, s: str) -> bool:
        digit_seen = exp_seen = dot_seen = False

        for i, c in enumerate(s):
            if c.isdigit():
                digit_seen = True
            elif c in ['+', '-']:
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif c in ['e', 'E']:
                if exp_seen or not digit_seen:
                    return False
                exp_seen = True
                digit_seen = False
            elif c == '.':
                if dot_seen or exp_seen:
                    return False
                dot_seen = True
            else:
                return False
        
        return digit_seen
