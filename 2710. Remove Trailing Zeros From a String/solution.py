class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_str = list(num)
        
        while num_str[-1] == '0':
            num_str.pop()
        
        return ''.join(num_str)
