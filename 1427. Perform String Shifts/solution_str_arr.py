class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def left_shift(str_arr, shift_amount):
            n = len(str_arr)
            shift_amount %= n

            for _ in range(shift_amount):
                first_char = str_arr[0]

                for j in range(n-1):
                    str_arr[j] = str_arr[j+1]
                
                str_arr[n-1] = first_char
            
            return ''.join(str_arr)
        
        def right_shift(str_arr, shift_amount):
            n = len(str_arr)
            shift_amount %= n

            for _ in range(shift_amount):
                last_char = str_arr[n-1]

                for j in range(n-1, 0, -1):
                    str_arr[j] = str_arr[j-1]
                
                str_arr[0] = last_char
            
            return ''.join(str_arr)
        
        mod_size = len(s)

        shift_num = 0

        for direction, amount in shift:
            if direction == 0:
                shift_num += amount
            else:
                shift_num -= amount
        
        shift_num %= mod_size

        if shift_num > 0:
            s = left_shift(list(s), shift_num)
        elif shift_num < 0:
            s = right_shift(list(s), - shift_num)
        
        return s
        
