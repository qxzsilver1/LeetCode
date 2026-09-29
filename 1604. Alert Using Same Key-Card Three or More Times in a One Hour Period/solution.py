class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        name_to_time = defaultdict(list)

        for name, hhmm in zip(keyName, keyTime):
            hr, minute = map(int, hhmm.split(':'))
            time = 60 * hr + minute
            name_to_time[name].append(time)
        
        res = []

        for name, times_list in name_to_time.items():
            times_list.sort()

            q = deque()

            for time in times_list:
                q.append(time)

                if q[-1] - q[0] > 60:
                    q.popleft()
                
                if len(q) >= 3:
                    res.append(name)
                    break
        
        return sorted(res)
