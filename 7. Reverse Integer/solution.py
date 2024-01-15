class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        output = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if output > MAX // 10 or (output == MAX // 10 and digit >= MAX % 10):
                return 0
            if output < MIN // 10 or (output == MIN // 10 and digit <= MIN % 10):
                return 0
            
            output = (output * 10) + digit
    
        return output
