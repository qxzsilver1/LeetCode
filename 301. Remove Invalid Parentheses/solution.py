class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        l, r = 0, 0

        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                r = r + 1 if l == 0 else r
                l = l - 1 if l > 0 else l
        
        res = {}

        def backtrack(idx, left_cnt, right_cnt, left_remain, right_remain, expr):
            if idx == len(s):
                if left_remain == 0 and right_remain == 0:
                    joined_str = ''.join(expr)
                    res[joined_str] = 1
            else:
                if (s[idx] == '(' and left_remain > 0) or (s[idx] == ')' and right_remain > 0):
                    backtrack(idx + 1, left_cnt, right_cnt, left_remain - (s[idx] == '('), right_remain - (s[idx] == ')'), expr)
                expr.append(s[idx])

                if s[idx] != '(' and s[idx] != ')':
                    backtrack(idx + 1, left_cnt, right_cnt, left_remain, right_remain, expr)
                elif s[idx] == '(':
                    backtrack(idx + 1, left_cnt + 1, right_cnt, left_remain, right_remain, expr)
                elif s[idx] == ')' and left_cnt > right_cnt:
                    backtrack(idx + 1, left_cnt, right_cnt + 1, left_remain, right_remain, expr)
                
                expr.pop()
        
        backtrack(0, 0, 0, l, r, [])

        return list(res.keys())
