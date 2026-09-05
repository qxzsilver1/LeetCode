class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger_change = [0] * 1001

        for t in trips:
            num_passengers, start, end = t
            passenger_change[start] += num_passengers
            passenger_change[end] -= num_passengers
        
        curr_passengers = 0

        for i in range(1001):
            curr_passengers += passenger_change[i]

            if curr_passengers > capacity:
                return False
        
        return True
