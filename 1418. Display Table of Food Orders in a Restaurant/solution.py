class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_to_food = defaultdict(list)
        food_items, table_numbers = set(), set()
        res = []

        for i, j, k in orders:
            table_to_food[j].append(k)
            food_items.add(k)
            table_numbers.add(j)
        
        for i in sorted(table_numbers):
            food_count = Counter(table_to_food[i])
            food_cnt = []

            for j in sorted(food_items):
                food_cnt += [str(food_count[j])]
            
            res.append([i] + food_cnt)
        
        res.sort(key = lambda x: int(x[0]))

        return [['Table'] + sorted(food_items)] + res
