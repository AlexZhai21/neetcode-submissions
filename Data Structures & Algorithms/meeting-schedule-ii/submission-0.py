"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        der_heap = []
        heapq.heapify(der_heap)
        intervals.sort(key= lambda Interval: Interval.start) #sorted by starting times nlogn for sorting
        n = len(intervals)
        for i in range(n):
            curr_int = intervals[i]
            start_t = curr_int.start
            end_t = curr_int.end
            if der_heap and der_heap[0] <= start_t: #der heap should be tracking end time of all the meetings, if the end time <= start tiem for current meeting: you can reuse that meeting room
                heapq.heappop(der_heap)
                heapq.heappush(der_heap, end_t) #logn time
            else:
                heapq.heappush(der_heap, end_t)

        return len(der_heap)
#nlogn

        