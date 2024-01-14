class TimeMap:

    def __init__(self):
        self.store = {} # key-value store with value of list of [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        output = ''
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][0] <= timestamp:
                output = values[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return output
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
