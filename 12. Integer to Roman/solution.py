class Solution:
    def intToRoman(self, num: int) -> str:
        roman_integer_list = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        res = ''

        for roman, int_val in reversed(roman_integer_list):
            if num // int_val:
                cnt = num // int_val
                res += roman * cnt
                num %= int_val
        
        return res
