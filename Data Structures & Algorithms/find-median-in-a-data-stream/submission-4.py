import heapq
class MedianFinder:

    def __init__(self):
        self.leng_max =0
        self.leng_min =0
        self.tracker_max = []
        self.tracker_min = []
        self.curr_median= None
   
        

    def addNum(self, num: int) -> None:
    

        if not self.curr_median or num <= self.curr_median:
            heapq.heappush(self.tracker_max, -num) 
            self.leng_max += 1
        else:
            heapq.heappush(self.tracker_min, num)
            self.leng_min+=1
        if self.leng_max- self.leng_min> 1:
            heapq.heappush(self.tracker_min, -1 * heapq.heappop(self.tracker_max))
            self.leng_max-=1
            self.leng_min+=1
        if self.leng_min - self.leng_max>1:
            heapq.heappush(self.tracker_max, -1 * heapq.heappop(self.tracker_min))
            self.leng_max+=1
            self.leng_min -=1
    
        if (self.leng_max+self.leng_min) %2 ==0:
            self.curr_median = (self.tracker_min[0] + -1 *self.tracker_max[0])/2
        else:
            if self.leng_max >self.leng_min:
                self.curr_median = -1 * self.tracker_max[0]
            else:
                self.curr_median = self.tracker_min[0]
    
    def findMedian(self) -> float:
        return self.curr_median

        
        