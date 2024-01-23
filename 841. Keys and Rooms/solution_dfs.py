class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        seen.add(0)

        def dfs(room):
            for key in rooms[room]:
                if key in seen:
                    continue
                
                seen.add(key)
                dfs(key)

        dfs(0)

        return len(seen) == len(rooms)
