class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        
        curr_sum = 0

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                curr_sum += i

                if i ** 2 != num:
                    curr_sum += num // i
        
        return curr_sum - num == num
