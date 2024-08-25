class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]
        
        for row in range(1, query_row + 1):
            curr_row = [0] * (row + 1)

            for i in range(row + 1):
                left_par = prev_row[i-1] if i > 0 else 0
                right_par = prev_row[i] if i < len(prev_row) else 0

                left_extra = max(0, left_par - 1)
                right_extra = max(0, right_par - 1)

                curr_row[i] = 0.5 * left_extra + 0.5 * right_extra
            
            prev_row = curr_row
        
        return min(1, prev_row[query_glass])
