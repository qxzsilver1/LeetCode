class BIT:
    def __init__(self, size):
        self.n = size + 2
        self.tree = [0] * self.n

    def update(self, index, delta):
        index += 1
        while index < self.n:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_update(self, left, right, delta):
        self.update(left, delta)
        self.update(right + 1, -delta)

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        bit = BIT(n)

        for left, right, d in shifts:
            delta = 1 if d == 1 else -1
            bit.range_update(left, right, delta)

        res = []
        
        for i in range(n):
            shift = bit.prefix_sum(i) % 26
            code = (ord(s[i]) - ord('a') + shift + 26) % 26
            res.append(chr(ord('a') + code))

        return ''.join(res)
