import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #kth largest = smallest element with a heap restricted to size k
        self.kHeap = nums
        heapq.heapify(self.kHeap)
        self.k = k


        

    def add(self, val: int) -> int:
        heapq.heappush(self.kHeap, val)
        while len(self.kHeap) > self.k:
            heapq.heappop(self.kHeap)
        
        return self.kHeap[0]

        
