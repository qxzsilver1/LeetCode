class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_cnt, late_consec_cnt = 0, 0
        prev_char = ''

        for i in range(len(s)):
            if s[i] == 'A':
                absent_cnt += 1
                if absent_cnt > 1:
                    return False
            elif s[i] == 'L':
                if prev_char == 'L':
                    late_consec_cnt += 1

                    if late_consec_cnt == 3:
                        return False
                else:
                    late_consec_cnt = 1
            
            prev_char = s[i]
        
        return True

                
