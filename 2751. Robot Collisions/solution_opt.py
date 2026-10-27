class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        idx_map = { p: i for i, p in enumerate(positions)}

        stack = [] # indices

        for p in sorted(positions):
            i = idx_map[p]

            if directions[i] == 'R':
                stack.append(i)
            else: # moving 'L'
                while stack and healths[i]:
                    j = stack.pop()

                    if healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[j]:
                        healths[j] -= 1
                        healths[i] = 0
                        stack.append(j)
                    else:
                        healths[i] = healths[j] = 0
        
        return [h for h in healths if h > 0]
