class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        l = 0

        res = 0

        for i in processorTime:
            res = max(res, i + max(tasks[l:l+4]))
            l += 4
        
        return res
