L, R = float("inf"), float("-inf")
        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)

        N = R - L + 1
        passChange = [0] * (N + 1)
        for passengers, start, end in trips:
            passChange[start - L] += passengers
            passChange[end - L] -= passengers

        curPass = 0
        for change in passChange:
            curPass += change
            if curPass > capacity:
                return False

        return True
