import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        minHeap = [] #should storethe groups (last added element, num_eleemnts)
        if groupSize == 1:
            return True
        for h in hand:
            if not minHeap:
                heapq.heappush(minHeap, [h, 1])
            else:
                top = heapq.heappop(minHeap)
                if h - top[0] != 1: 
                    heapq.heappush(minHeap, [h, 1])
                else:
                    top[0]= h
                    top[1] = top[1] + 1
                if top[1] <groupSize:
                    heapq.heappush(minHeap, top)
        return len(minHeap)==0




        