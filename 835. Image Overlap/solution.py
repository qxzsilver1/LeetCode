class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)

        def shiftAndCount(x_shift, y_shift, M, R):
            left_shift_cnt, right_shift_cnt = 0, 0

            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_cnt += 1
                    
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_cnt += 1
            
            return max(left_shift_cnt, right_shift_cnt)
        
        max_overlaps = 0

        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shiftAndCount(x_shift, y_shift, img1, img2))
                max_overlaps = max(max_overlaps, shiftAndCount(x_shift, y_shift, img2, img1))
        
        return max_overlaps
