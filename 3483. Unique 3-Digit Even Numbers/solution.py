class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq_count = [0] * 10

        for d in digits:
            freq_count[d] += 1
        
        cnt = 0

        for hundreds in range(1, 10):
            if freq_count[hundreds] == 0:
                continue
            freq_count[hundreds] -= 1

            for tens in range(0, 10):
                if freq_count[tens] == 0:
                    continue
                freq_count[tens] -= 1

                for ones in range(0, 9, 2):
                    if freq_count[ones] > 0:
                        cnt += 1
                
                freq_count[tens] += 1
            
            freq_count[hundreds] += 1
        
        return cnt
