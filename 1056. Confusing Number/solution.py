class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        invert_num = 0

        n_copy = n

        while n_copy:
            res = n_copy % 10

            if res not in invert_map:
                return False
            
            invert_num = invert_num * 10 + invert_map[res]
            n_copy //= 10
        
        return invert_num != n
