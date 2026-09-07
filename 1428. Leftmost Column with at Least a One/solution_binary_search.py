# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROWS, COLS = binaryMatrix.dimensions()

        smallest_idx = COLS

        for row in range(ROWS):
            l, r = 0, COLS - 1

            while l < r:
                m = (l + r) // 2

                if binaryMatrix.get(row, m) == 0:
                    l = m + 1
                else:
                    r = m
            
            if binaryMatrix.get(row, l) == 1:
                smallest_idx = min(smallest_idx, l)
            
        return -1 if smallest_idx == COLS else smallest_idx
