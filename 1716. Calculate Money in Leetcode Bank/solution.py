class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks = n // 7
        low = 28
        high = low + 7 * (num_weeks - 1)
        output = (low + high) * num_weeks // 2

        monday = num_weeks + 1

        for i in range(n % 7):
            output += i + monday

        return output
