class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        output = ''

        for r in range(numRows):
            incr = 2 * (numRows - 1)

            for i in range(r, len(s), incr):
                output += s[i]

                if r > 0 and r < numRows - 1 and i + incr - 2 * r < len(s):
                    output += s[i + incr - 2 * r]
        
        return output
