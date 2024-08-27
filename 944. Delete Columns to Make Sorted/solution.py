class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ROWS, COLS = len(strs), len(strs[0])

        num_cols = 0

        for c in range(COLS):
            curr_char = 'a'

            for r in range(ROWS):
                if strs[r][c] < curr_char:
                    num_cols += 1
                    break
                
                curr_char = strs[r][c]
        
        return num_cols
