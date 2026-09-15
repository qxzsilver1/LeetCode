class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        n = len(num)
        res = []

        def backtrack(idx, prev_operand, curr_operand, val, input_str):
            if idx == n:
                if val == target and curr_operand == 0:
                    res.append(''.join(input_str[1:]))
                return
            
            curr_operand = curr_operand * 10 + int(num[idx])
            str_operand = str(curr_operand)

            if curr_operand > 0:
                backtrack(idx + 1, prev_operand, curr_operand, val, input_str)
            
            input_str.append('+')
            input_str.append(str_operand)
            
            backtrack(idx + 1, curr_operand, 0, val + curr_operand, input_str)
            
            input_str.pop(); input_str.pop()

            if input_str:
                input_str.append('-')
                input_str.append(str_operand)

                backtrack(idx + 1, - curr_operand, 0, val - curr_operand, input_str)

                input_str.pop(); input_str.pop()

                input_str.append('*')
                input_str.append(str_operand)

                backtrack(idx + 1, curr_operand * prev_operand, 0, val - prev_operand + (curr_operand * prev_operand), input_str)

                input_str.pop(); input_str.pop()
        
        backtrack(0, 0, 0, 0, [])

        return res
