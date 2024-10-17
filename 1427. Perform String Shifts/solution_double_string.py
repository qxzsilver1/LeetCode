class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def leftRotate(s, amt):
            n = len(s)
            tmp = s + s
            return tmp[amt:n+amt]
        
        def rightRotate(s, amt):
            return leftRotate(s, len(s) - amt)
        
        mod_size = len(s)

        shift_num = 0

        for direction, amount in shift:
            if direction == 0:
                shift_num += amount
            else:
                shift_num -= amount
        
        shift_num %= mod_size

        if shift_num > 0:
            s = leftRotate(s, shift_num)
        elif shift_num < 0:
            s = rightRotate(s, - shift_num)
        
        return s
        
