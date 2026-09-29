class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        left, right = float('-inf'), float('inf')
        seen = set()

        for x, y in points:
            left = max(left, x)
            right = min(right, x)
            seen.add((x, y))

        axis = (left + right) / 2

        for x, y in points:
            mirror = 2 * axis - x
            
            if (mirror, y) not in seen:
                return False

        return True
