import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_min = []
        #by default this is min heap
        heapq.heapify(k_min)
        for n in nums:
            heapq.heappush(k_min, n)
            if len(k_min) > k: #this means the smallest item in k_min has >= k items larger than it, when we know that the kth element an only hae k - 1 elements larger than it, so smallest is invalid
                heapq.heappop(k_min) #remove this elemeent from it
        return heapq.heappop(k_min)
            








        #kth largest in the array means k -1 larger than it
        #{2: 3}


        