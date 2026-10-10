class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in intervals:
            if not ans:
                ans.append(i)
            elif ans[-1][-1] >= i[0]: #overlapping, update the most recent ones
                ans[-1][-1] = max(ans[-1][-1], i[1])
            else:
                ans.append(i)
        return ans

        