class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        enter_pool, exit_pool = deque(), deque()

        curr_time = 0

        prev_state = 1

        res = [0] * len(arrival)

        i = 0

        while i < len(arrival) or enter_pool or exit_pool:
            # add all of current clients
            while i < len(arrival) and arrival[i] <= curr_time:
                if state[i]==0:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i+=1 
            
            # optimization for skipping time (the wait between the current time and next client might be long)
            if (not (enter_pool or exit_pool)) and prev_state == 1:
                curr_time = arrival[i]
                continue
            
            if prev_state == 1:
                if exit_pool:
                    res[exit_pool.popleft()] = curr_time
                elif enter_pool:
                    res[enter_pool.popleft()] = curr_time
                    prev_state = 0
            else:
                if enter_pool:
                    res[enter_pool.popleft()] = curr_time
                elif exit_pool:
                    res[exit_pool.popleft()] = curr_time
                    prev_state = 1
                else: 
                    prev_state = 1
            
            curr_time += 1

        return res 
