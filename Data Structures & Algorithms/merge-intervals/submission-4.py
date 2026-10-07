class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= ans[-1][-1]: #this means there is an overlap
                ans[-1][-1] = max(ans[-1][-1], i[-1])
            else:
                ans.append(i)
        return ans

        