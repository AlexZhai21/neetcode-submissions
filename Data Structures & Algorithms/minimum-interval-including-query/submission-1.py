import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        unsorted_query = queries
        queries = sorted(queries)
        tracker = {} #query: answer, use this to reconstruct
        der_heap = []
        der_i = 0
        for q in queries:
            tracker[q] = -1
        i = intervals[der_i]
        for q in queries:
            # while i[0] <= q: #if the current starting point is less than q, this interval can hold q
            #     to_push = [i[1] - i[0] + 1] + i
            #     heapq.heappush(der_heap, to_push)
            #     der_i += 1\
            while der_i < len(intervals) and intervals[der_i][0] <= q:
                i = intervals[der_i]
                heapq.heappush(der_heap, [i[1] - i[0] + 1] + i)
                der_i += 1
                if der_i < len(intervals):
                    i = intervals[der_i]
                else:
                    break
            while der_heap:
                if der_heap[0][2] < q:
                    heapq.heappop(der_heap) #remove that interval, its useless from now on since we sorted queries so every other query like if an interval is already too smallf or this q, because every other q is even largr, the next qs woulnt fit in this interval too
                else: #this is the smallest thing that stores q, WE ONLY PUSHED THINGS ONTO THE QUERY THAT HAVE A STARTING POINT <= Q
                    tracker[q] = der_heap[0][0]
                    break
        output = []
        for q in unsorted_query:
            output.append(tracker[q])
        return output



                