class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x: x[1])
        max_heap = []

        time = 0

        for c in courses:
            if time + c[0] <= c[1]:
                heapq.heappush(max_heap, - c[0])
                time += c[0]
            elif max_heap and max_heap[0] < -c[0]:
                time += c[0] - (- heapq.heappop(max_heap))
                heapq.heappush(max_heap, - c[0])
        
        return len(max_heap)
