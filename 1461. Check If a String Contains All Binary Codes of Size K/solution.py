class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_code_set = set()

        for i in range(len(s) - k + 1):
            binary_code_set.add(s[i:i+k])
        
        return len(binary_code_set) == 2 ** k
