class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        deposit = 1
        output = 0

        while day < n:
            output += deposit
            deposit += 1
            day += 1

            if day % 7 == 0:
                deposit = day // 7 + 1
        
        return output
