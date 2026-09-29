class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n
    
    def _check_diagonal(self, player: int) -> bool:
        for row in range(self.n):
            if self.board[row][row] != player:
                return False
        return True

    def _check_anti_diagonal(self, player: int) -> bool:
        for row in range(self.n):
            if self.board[row][self.n - row - 1] != player:
                return False
        return True

    def _check_column(self, col: int, player: int) -> bool:
        for row in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def _check_row(self, row: int, player: int) -> bool:
        for col in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self._check_row(row, player) or self._check_column(col, player) or (row == col and self._check_diagonal(player)) or (col == self.n - row - 1 and self._check_anti_diagonal(player)):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
