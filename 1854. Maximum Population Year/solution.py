class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop_change = {}

        for i in range(len(logs)):
            birth_yr, death_yr = tuple(logs[i])

            pop_change[birth_yr] = pop_change.get(birth_yr, 0) + 1
            pop_change[death_yr] = pop_change.get(death_yr, 0) - 1
        
        curr_pop, max_pop = 0, 0
        year = 1950

        sorted_pop_change = { k: pop_change[k] for k in sorted(pop_change) }

        for k,v in sorted_pop_change.items():
            curr_pop += v

            if curr_pop > max_pop:
                max_pop = curr_pop
                year = k
        
        return year
