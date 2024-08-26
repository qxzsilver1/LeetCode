class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])

        visited = set()

        q = deque()

        def addRooms(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                rooms[r][c] = dist

                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            
            dist += 1
