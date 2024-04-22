class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_alphabet = 26
        res = ''

        while columnNumber > 0:
            offset = (columnNumber - 1) % num_alphabet
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // num_alphabet
        
        return res[::-1]
