class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency_mat = defaultdict(list)

        for i in range(n):
            adjacency_mat[manager[i]].append(i)
        
        q = deque([(headID, 0)])
        res = 0
        
        while q:
            employee_id, time = q.popleft()
            res = max(res, time)

            for emp in adjacency_mat[employee_id]:
                q.append((emp, time + informTime[employee_id]))
        
        return res
