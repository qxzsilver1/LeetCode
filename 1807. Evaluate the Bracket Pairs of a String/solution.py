class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        convert_dict = dict(knowledge)

        res = []
        start = -1

        for i, c in enumerate(s):
            if c == '(':
                start = i
            elif c == ')':
                res.append(convert_dict.get(s[start + 1:i], '?'))
                start = -1
            elif start < 0:
                res.append(c)
        
        return ''.join(res)
