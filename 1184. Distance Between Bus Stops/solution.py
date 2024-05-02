class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            start, destination = destination, start
        
        sum_clockwise = sum(distance[start:destination])
        sum_counterclockwise = sum(distance) - sum_clockwise

        return min(sum_clockwise, sum_counterclockwise)
