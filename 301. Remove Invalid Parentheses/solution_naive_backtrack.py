class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        min_removed = float('inf')
        valid_expressions = set()

        def remaining(idx, left_cnt, right_cnt, expr, remain_cnt):
            nonlocal min_removed
            nonlocal valid_expressions
            
            if idx == len(s):
                if left_cnt == right_cnt:
                    if remain_cnt <= min_removed:
                        possible_str = ''.join(expr)

                        if remain_cnt < min_removed:
                            valid_expressions = set()
                            min_removed = remain_cnt
                        
                        valid_expressions.add(possible_str)
            else:
                curr_char = s[idx]

                if curr_char != '(' and curr_char != ')':
                    expr.append(curr_char)
                    remaining(idx + 1, left_cnt, right_cnt, expr, remain_cnt)
                    expr.pop()
                else:
                    remaining(idx + 1, left_cnt, right_cnt, expr, remain_cnt + 1)
                    expr.append(curr_char)

                    if s[idx] == '(':
                        remaining(idx + 1, left_cnt + 1, right_cnt, expr, remain_cnt)
                    elif right_cnt < left_cnt:
                        remaining(idx + 1, left_cnt, right_cnt + 1, expr, remain_cnt)

                    expr.pop()
        
        remaining(0, 0, 0, [], 0)

        return list(valid_expressions)
