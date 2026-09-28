class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        steps = 0

        while target > 0:
            steps += 1
            target -= steps
        
        return steps if target % 2 == 0 else steps + 1 + steps % 2
