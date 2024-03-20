class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        doms = list(dominoes)
        q = deque()

        for i, d in enumerate(doms):
            if d != '.':
                q.append((i, d))
        
        while q:
            i, d = q.popleft()
        
            if d == 'L':
                if i > 0 and doms[i - 1] == '.':
                    q.append((i-1, 'L'))
                    doms[i-1] = 'L'
            elif d == 'R':
                if i + 1 < len(doms) and doms[i + 1] == '.':
                    if i + 2 < len(doms) and doms[i + 2] == 'L':
                        q.popleft()
                    else:
                        q.append((i+1, 'R'))
                        doms[i+1] = 'R'
        
        return ''.join(doms)
