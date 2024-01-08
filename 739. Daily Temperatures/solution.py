class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx

            stack.append(i)
        
        return output
                
