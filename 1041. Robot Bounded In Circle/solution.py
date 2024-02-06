class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x_vec, y_vec = 0, 1
        x, y = 0, 0

        for d in instructions:
            if d == 'G':
                x, y = x + x_vec, y + y_vec
            elif d == 'L':
                x_vec, y_vec = -1*y_vec, x_vec
            else:
                x_vec, y_vec = y_vec, -1 * x_vec
        
        return (x, y) == (0, 0) or (x_vec, y_vec) != (0, 1)
