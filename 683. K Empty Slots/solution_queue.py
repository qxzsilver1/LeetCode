class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n

        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
        
        q = MinQueue()
        res = n

        for i, day in enumerate(days):
            q.append(day)

            if k <= i < n - 1:
                q.popleft()

                if k == 0 or (days[i - k] < q.min() and q.min() > days[i + 1]):
                    res = min(res, max(days[i - k], days[i + 1]))
        
        return res if res < n else -1
