class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_dict = defaultdict(int)
        res = []

        for n in nums:
            row = count_dict[n]

            if len(res) == row:
                res.append([])
            
            res[row].append(n)
            count_dict[n] += 1
        
        return res
