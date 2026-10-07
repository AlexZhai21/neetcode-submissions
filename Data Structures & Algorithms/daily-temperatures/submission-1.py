from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tracker = deque()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
        
            while len(tracker) > 0 and tracker[-1][0] < temperatures[i]:
                result[tracker[-1][1]] = i - tracker[-1][1]
                tracker.pop()
            tracker.append((temperatures[i], i))
        return result


        