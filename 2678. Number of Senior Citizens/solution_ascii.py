class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for d in details:
            tens = ord(d[11]) - ord('0')
            ones = ord(d[12]) - ord('0')

            age = 10 * tens + ones
            
            if age > 60:
                res += 1
        
        return res
