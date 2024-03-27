class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count_dict = defaultdict(int)
        
        l = 0
        curr_total, res = 0, 0

        for r in range(len(fruits)):
            count_dict[fruits[r]] += 1
            curr_total += 1

            while len(count_dict) > 2:
                f = fruits[l]
                count_dict[f] -= 1
                curr_total -= 1

                l += 1

                if not count_dict[f]:
                    count_dict.pop(f)

            res = max(res, curr_total)
        
        return res
