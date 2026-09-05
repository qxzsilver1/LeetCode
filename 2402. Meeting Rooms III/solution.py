class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = [] # (end_time, room_number)
        room_counts = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room_num = heapq.heappop(used)
                heapq.heappush(available, room_num)
            
            if not available:
                end_time, room_num = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room_num)
            
            room_num = heapq.heappop(available)
            heapq.heappush(used, (end, room_num))
            room_counts[room_num] += 1


        return room_counts.index(max(room_counts))
