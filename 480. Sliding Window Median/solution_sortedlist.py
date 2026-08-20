class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []

        max_set = SortedList(key= lambda x: (-x[0], -x[1]))
        min_set = SortedList(key= lambda x: (x[0], x[1]))

        for i in range(k):
            min_set.add((nums[i], i))
        
        for _ in range(k // 2):
            top = min_set[0]
            max_set.add(top)
            min_set.remove(top)
        
        median = min_set[0][0] if k % 2 else (max_set[0][0] + min_set[0][0]) / 2

        res.append(median)

        l, r = 0, k

        while r < len(nums):
            add_num = (nums[r], r)
            remove_num = (nums[l], l)

            removed_from_min_set = True

            if remove_num in max_set:
                max_set.remove(remove_num)
                removed_from_min_set = False
            else:
                min_set.remove(remove_num)
            
            if removed_from_min_set:
                max_set.add(add_num)
                top = max_set[0]
                min_set.add(top)
                max_set.remove(top)
            else:
                min_set.add(add_num)
                top = min_set[0]
                max_set.add(top)
                min_set.remove(top)
            
            median = min_set[0][0] if k % 2 else (max_set[0][0] + min_set[0][0]) / 2

            res.append(median)

            l += 1
            r += 1
        
        return res
