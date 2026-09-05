class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_y_list = [0, 0]

        move_map = { 'U': (1, 1), 'D': (1, -1), 'L': (0, -1), 'R': (0, 1) }

        for move in moves:
            idx, direction = move_map[move]
            x_y_list[idx] += direction
        
        return x_y_list[0] == x_y_list[1] == 0
