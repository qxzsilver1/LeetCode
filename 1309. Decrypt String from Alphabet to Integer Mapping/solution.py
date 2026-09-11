class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''

        curr_num = ''

        i = len(s) - 1

        while i > -1:
            if s[i] == '#':
                while len(curr_num) != 2:
                    i -=1
                    curr_num = s[i] + curr_num
                
                res = chr(int(curr_num) + ord('a') - 1) + res
                curr_num = ''
            else:
                res = chr(int(s[i]) + ord('a') - 1) + res
            
            i -= 1
        
        return res
