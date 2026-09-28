class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        prefix_sum = [0] * len(words)
        curr_total = 0

        for i in range(len(words)):
            curr_word = words[i]

            if curr_word[0] in vowels and curr_word[len(curr_word) - 1] in vowels:
                curr_total += 1
            prefix_sum[i] = curr_total
        
        for i in range(len(queries)):
            curr_query = queries[i]

            res[i] = prefix_sum[curr_query[1]] - (0 if curr_query[0] == 0 else prefix_sum[curr_query[0] - 1])
        
        return res
