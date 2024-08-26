class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        q = deque()
        q.append(('0000', 0)) # lock position, number of turns

        visited = set(deadends)

        def children(lock):
            res = []

            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

                digit = str((int(lock[i]) -1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res

        while q:
            lock_pos, num_turns = q.popleft()

            if lock_pos == target:
                return num_turns
            
            for child in children(lock_pos):
                if child not in visited:
                    visited.add(child)
                    q.append((child, num_turns + 1))
        
        return -1
