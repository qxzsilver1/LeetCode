class Solution:
    def thousandSeparator(self, n: int) -> str:
        sep_str = ''

        while n // 1000:
            if n % 1000 > 99:
                sep_str = '.' + str(n % 1000) + sep_str
            elif n % 1000 > 9:
                sep_str = '.' + '0' + str(n % 1000) + sep_str
            else:
                sep_str = '.' + '00' + str(n % 1000) + sep_str
            n //= 1000
        
        sep_str = str(n % 1000) + sep_str
        
        return sep_str
