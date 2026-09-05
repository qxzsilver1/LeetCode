class Solution:
    def interpret(self, command: str) -> str:
        mapping = { 'G': 'G', '()': 'o', '(al)': 'al' }

        tmp, res = '', ''

        for i in range(len(command)):
            tmp += command[i]

            if tmp in mapping:
                res += mapping[tmp]
                tmp = ''
        
        return res
