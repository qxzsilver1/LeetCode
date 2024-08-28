class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        
        evens = sorted([(j, i) for i, j in enumerate(num_str) if not int(j) % 2], reverse=True)
        evens_indices = sorted([i for j, i in evens])

        evens_index_map = { k: v[0] for v, k in zip(evens, evens_indices) }

        odds = sorted([(j, i) for i, j in enumerate(num_str) if int(j) % 2], reverse=True)
        odds_indices = sorted([i for j, i in odds])

        odds_index_map = { k: v[0] for v, k in zip(odds, odds_indices) }

        total_dict = evens_index_map | odds_index_map

        res = [-1] * len(num_str)

        for i in range(len(num_str)):
            res[i] = total_dict[i]

        return int(''.join(res))
