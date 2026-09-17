class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = n = len(words)

        for i, w in enumerate(words):
            if w == target:
                res = min(res, abs(i - startIndex), n - abs(i - startIndex))
        
        return res if res < n else -1
