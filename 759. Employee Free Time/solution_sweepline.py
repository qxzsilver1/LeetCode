"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        opens, closes = 0, 1

        events = []

        for emp in schedule:
            for interval in emp:
                events.append((interval.start, opens))
                events.append((interval.end, closes))
        
        events.sort()

        res = []

        prev = None
        balance = 0

        for t, cond in events:
            if balance == 0 and prev is not None:
                res.append(Interval(prev, t))
            
            balance += 1 if cond is opens else -1
            prev =t
        
        return res
