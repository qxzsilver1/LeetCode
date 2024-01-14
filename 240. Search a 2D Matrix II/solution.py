class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        right = cols - 1

        while top < rows and right >= 0:
            if matrix[top][right] == target:
                return True
            elif matrix[top][right] < target:
                top += 1
            else:
                right -= 1
        
        return False
