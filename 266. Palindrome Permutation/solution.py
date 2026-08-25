class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)

        odd_count = sum(val % 2 for val in count.values())

        return odd_count <= 1
