class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num_alphabet = 26
        
        column = 0
        multiplier = 1

        idx = len(columnTitle) - 1

        while idx > -1:
            column += (ord(columnTitle[idx]) - ord('A') + 1) * multiplier
            multiplier *= num_alphabet
            
            idx -= 1
        
        return column
