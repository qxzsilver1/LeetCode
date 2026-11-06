class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'
            else:
                write_a = a >= b
            
            if write_a:
                a -= 1
                res.append('a')
            else:
                b -= 1
                res.append('b')
        
        return ''.join(res)
