from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        cnt = [0] * k

        busy = []
        free = list(range(k))

        for i, start in enumerate(arrival):
            # Remove free servers from 'busy', modify their IDs and
            # add them to 'free'
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                heapq.heappush(free, i + (server_id - i) % k)

            # Get the original server ID by taking the remainder of
            # the modified ID to k.
            if free:
                busy_id = heapq.heappop(free) % k
                heapq.heappush(busy, (start + load[i], busy_id))
                cnt[busy_id] += 1
        
        # Find the servers that have the maximum workload.
        max_job = max(cnt)
        
        return [i for i, n in enumerate(cnt) if n == max_job]
