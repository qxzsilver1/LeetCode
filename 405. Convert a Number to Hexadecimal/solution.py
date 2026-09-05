class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        hex_map = '0123456789abcdef'

        res = ''

        for i in range(8):
            n = num & 15 # 1111b - in binary 15 0b1111 instead of hexadecimal
            c = hex_map[n]

            res = c + res
            num >>= 4

            if num == 0:
                break
        
        return res
