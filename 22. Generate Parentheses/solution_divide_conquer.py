class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        
        res = []

        for left_cnt in range(n):
            left_strings = self.generateParenthesis(left_cnt)
            right_strings = self.generateParenthesis(n - 1 - left_cnt)

            for left_str in left_strings:
                for right_str in right_strings:
                    res.append('(' + left_str + ')' + right_str)
        
        return res
