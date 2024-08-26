class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []

        open_parenthesis_count = 0

        for c in s:
            if c == '(':
                res.append(c)
                open_parenthesis_count += 1
            elif c == ')' and open_parenthesis_count > 0:
                res.append(c)
                open_parenthesis_count -= 1
            elif c != ')':
                res.append(c)
        
        res_updated = []

        for c in res[::-1]:
            if c == '(' and open_parenthesis_count > 0:
                open_parenthesis_count -= 1
            else:
                res_updated.append(c)
        
        return ''.join(res_updated[::-1])
