class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        line_sweeper = [0] * n

        for i in bookings:
            start, end = i[0] - 1, i[1] 

            line_sweeper[start] += i[2]

            if end < n:
                line_sweeper[end] -= i[2]
        
        prefix_sum = [line_sweeper[0]]

        for i in range(1, n):
            prefix_sum.append(prefix_sum[i-1] + line_sweeper[i])
        
        return prefix_sum
