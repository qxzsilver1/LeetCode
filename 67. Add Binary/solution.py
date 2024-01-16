class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry

            digit_char = str(total % 2)
            res = digit_char + res

            carry = total // 2
        
        if carry:
            res = '1' + res
        
        return res
