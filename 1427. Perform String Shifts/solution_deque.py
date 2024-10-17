class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def shiftByAmount(s, shift_amount):
            char_deque = deque(s)
            char_deque.rotate(shift_amount)

            return ''.join(char_deque)
        
        mod_size = len(s)

        shift_num = 0

        for direction, amount in shift:
            if direction == 0:
                shift_num -= amount
            else:
                shift_num += amount
        
        shift_num %= mod_size

        s = shiftByAmount(s, shift_num) if shift_num != 0 else s
        
        return s
        
