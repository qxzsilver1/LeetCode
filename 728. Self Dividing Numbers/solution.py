class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        
        def isSelfDividing(num):
            num_divisible = dict()

            num_curr = num
            
            while num_curr:
                curr_digit = num_curr % 10

                if curr_digit == 0 or num % curr_digit != 0:
                    return False
                
                if curr_digit not in num_divisible and num % curr_digit == 0:
                    num_divisible[curr_digit] = True
                
                if len(num_divisible) == 9:
                    return True

                num_curr = num_curr // 10
            return True
        
        for i in range(left, right + 1):
            if isSelfDividing(i):
                res.append(i)
        
        return res
