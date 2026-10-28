class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        ROWS, COLS = len(image), len(image[0])

        def boundary(lo, hi, is_row, wanted):
            while lo < hi:
                m = (lo + hi) // 2
                present = any(image[m][j] == '1' for j in range(COLS)) if is_row else any(image[i][m] == '1' for i in range(ROWS))

                if present == wanted:
                    hi = m
                else:
                    lo = m + 1
            
            return lo
        
        top = boundary(0, x, True, True)
        bottom = boundary(x, ROWS, True, False)
        left = boundary(0, y, False, True)
        right = boundary(y, COLS, False, False)
        
        return (bottom - top) * (right - left)
