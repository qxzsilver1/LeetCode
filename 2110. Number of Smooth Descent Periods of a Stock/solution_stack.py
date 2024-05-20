class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0

        stack = []

        for i, p in enumerate(prices):
            ctr = 0
            idx = 1

            if stack and stack[-1][1] - p != 1:
                while stack:
                    j, n = stack.pop()
                    ctr += idx
                    idx += 1
            
            res += ctr
            
            if not stack or stack and stack[-1][1] - p == 1:
                stack.append((i, p))
                continue
        
        ctr = 0
        idx = 1

        while stack:
            k, n = stack.pop()
            ctr += idx
            idx += 1
        
        res += ctr
        
        return res
            


