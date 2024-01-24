class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        string_set = set()
        string_set.add(s1)
        string_set.add(s2)
        string_set.add(s3)
        
        len1, len2, len3 = len(s1), len(s2), len(s3)
        len_matrix = [len1, len2, len3]

        idx, min_len = -1, float('inf')

        for i, l in enumerate(len_matrix):
            if min_len > l:
                min_len = l
                idx = i
        
        shortest_str = ''

        if idx == 0:
            shortest_str = s1
        elif idx == 1:
            shortest_str = s2
        elif idx == 2:
            shortest_str = s3

        non_shortest_str_set = string_set.difference(shortest_str)
        non_shortest_str_list = list(non_shortest_str_set)
        non_shortest_str_list_len = len(non_shortest_str_list)
        
        for j in range(min_len):
            for non_short_str in non_shortest_str_list:
                if shortest_str[j] != non_short_str[j]:
                    return -1
                
                continue
        
        res = 0

        for k in range(non_shortest_str_list_len):
            res += len(non_shortest_str_list[k]) - min_len
        
        return res
        
