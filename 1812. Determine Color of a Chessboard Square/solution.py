class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = ord(coordinates[0]) - ord('a') + 1, int(coordinates[1])

        return (x + y) % 2
