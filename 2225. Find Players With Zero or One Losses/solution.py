class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]

        lose_count = defaultdict(int)

        for m in matches:
            lose_count[m[0]] += 0
            lose_count[m[1]] += 1
        
        for k, v in lose_count.items():
            if v == 1 or v == 0:
                answer[v].append(k)
        
        for l in answer:
            l.sort()
        
        return answer
