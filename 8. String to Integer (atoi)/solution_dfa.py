class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        val, state, pos, sign = 0, 0, 0, 1
        
        # state:
        # 0: initial state
        # 1: '-' or '+' encountered from state 0
        # 2: digits encountered
        # final state: any character other than digit or -/+ encounter from initial state

        while pos < len(s):
            curr = s[pos]

            if state == 0:
                if curr == ' ':
                    state = 0
                elif curr == '-' or curr == '+':
                    state = 1
                    sign = -1 if curr == '-' else 1
                elif curr.isdigit():
                    state = 2
                    val *= 10
                    val += int(curr)
                else:
                    return 0
            elif state == 1:
                if curr.isdigit():
                    state = 2
                    val *= 10
                    val += int(curr)
                else:
                    return 0
            elif state == 2:
                if curr.isdigit():
                    state = 2
                    val *= 10
                    val += int(curr)
                else:
                    break
            else:
                return 0
            
            pos += 1
        
        val *= sign
        val = min(val, 2 ** 31 - 1)
        val = max(- 2 ** 31, val)
        
        return val
        
