class Solution:
    def countCommas(self, n: int) -> int:
        res = 0

        comparison_number = 1000
        
        while comparison_number <= n:
            res += n - comparison_number + 1
            comparison_number *= 1000
         
        return res
