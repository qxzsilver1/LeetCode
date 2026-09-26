class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        idx = 0
        n = len(expression)

        def isLetter(c):
            return 'a' <= c <= 'z'
        
        def expr():
            nonlocal idx
            ret = set()

            while True:
                ret |= term()

                if idx < n and expression[idx] == ',':
                    idx += 1
                    continue
                else:
                    break
            
            return ret
        
        def term():
            nonlocal idx
            ret = {''}

            while idx <n and (expression[idx] == '{' or isLetter(expression[idx])):
                sub = item()
                tmp = set()

                for left in ret:
                    for right in sub:
                        tmp.add(left + right)
                
                ret = tmp
            return ret
        
        def item():
            nonlocal idx
            ret = set()

            if expression[idx] == '{':
                idx += 1
                ret = expr()
            else:
                ret = {expression[idx]}
            
            idx += 1

            return ret
        
        ret = expr()

        return sorted(list(ret))
