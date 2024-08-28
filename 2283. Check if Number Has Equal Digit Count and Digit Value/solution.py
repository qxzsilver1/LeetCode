class Solution:
    def digitCount(self, num: str) -> bool:
        count_dict = Counter(num)
        
        array_idx_dict = {str(i): int(n) for i, n in enumerate(num) }
        
        for k in array_idx_dict:
            if k not in count_dict and array_idx_dict[k] == 0 or k in count_dict and array_idx_dict[k] == count_dict[k]:
                continue
            else:
                return False
        
        return True
