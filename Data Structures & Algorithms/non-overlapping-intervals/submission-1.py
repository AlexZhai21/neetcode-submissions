class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        inter = None
        for i in intervals:
            i_s = i[0]
            i_e = i[1]
            if not inter:
                inter = i
            else:
                if inter[1] > i_s: #if the current built interval contains the next one
                    if inter[1] > i_e:
                        inter = i
                    
                    ans += 1
                else: #this means no overlap
                    inter = i
        print(intervals)
        return ans
#[1, 10], [5, 11] #always remvoe the one that extends further