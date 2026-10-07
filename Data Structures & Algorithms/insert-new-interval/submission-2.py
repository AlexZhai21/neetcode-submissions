class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #o(n) time, insert takes n time but we only do it once
        inserted = False
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]: #insert it right before i
                intervals.insert(i, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)
        ans = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= ans[-1][-1]:
                ans[-1][-1] = max(ans[-1][-1], i[-1])
            else:
                ans.append(i)
        return ans

        

        
        
        