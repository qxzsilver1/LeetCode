class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        def add(a, b):
            if not a or not b:
                return a or b
            
            return add(a ^ b, (a & b) << 1)
        
        if a * b < 0: # assuming a < 0, b > 0
            if a > 0: # switch order of b and a to meet assumption condition
                return self.getSum(b, a)
            
            if add(~a, 1) == b: # -a == b
                return 0
            
            if add(~a, 1) < b: # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1) # add -a and -b
        
        return add(a, b)
