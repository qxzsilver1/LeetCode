class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        seen = set()
        seen.add(0)

        while q:
            room = q.popleft()

            for key in rooms[room]:
                if key in seen:
                    continue
                
                seen.add(key)
                q.append(key)
                
        return len(seen) == len(rooms)
