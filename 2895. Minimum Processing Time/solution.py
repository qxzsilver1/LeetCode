class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()

        l, r = 0, 0

        res = 0

        for i in processorTime:
            r = l + 4
            res = max(res, i + max(tasks[l:r]))
            l = r
        
        return res
