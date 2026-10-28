class Solution:
    def badSensor(self, sensor1: list[int], sensor2: list[int]) -> int:
        n = len(sensor1)

        i = 0

        while i < n and sensor1[i] == sensor2[i]:
            i += 1
        
        if i == n:
            return -1
        
        first = sensor1[-1] != sensor2[i] and all(sensor1[j] == sensor2[j + 1] for j in range(i, n - 1))
        second = sensor2[-1] != sensor1[i] and all(sensor2[j] == sensor1[j + 1] for j in range(i, n - 1))

        return (1 if first else 2) if first != second else -1
