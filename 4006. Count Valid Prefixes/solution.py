class Solution:
    def countValidPrefixes(self, s: str) -> int:
        num_balance = 0
        res = 0

        for c in s:
            num_balance = num_balance + 1 if c == '1' else num_balance - 1

            if -1 <= num_balance <= 1:
                res += 1
        
        return res
