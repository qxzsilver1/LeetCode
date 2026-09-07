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

        curr_row = 0
        curr_col = COLS - 1

        while curr_row < ROWS and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 0:
                curr_row += 1
            else:
                curr_col -= 1
        
        return curr_col + 1 if curr_col != COLS - 1 else -1
