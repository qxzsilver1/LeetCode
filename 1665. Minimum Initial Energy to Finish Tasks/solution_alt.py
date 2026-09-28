class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key= lambda x: x[1] - x[0], reverse= True)

        res = 0
        remaining = 0

        for task in tasks:
            if remaining <= task[1]:
                res += task[1] - remaining
            
            remaining = max(task[1] - task[0], remaining - task[0])
        
        return res
