import heapq
class MinStack:

    def __init__(self):
        self.minHeap = []
        self.derStack = []
        #if you want to push a number thats > than the current min on the minHeap, theres no point in adding it, since by the nature of the stack even if you do a bunch of pops, that larger value would get popped first
        #by controlling the size of the minJ
        

    def push(self, val: int) -> None:
        self.derStack.append(val)
        if not self.minHeap or val <= self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
        #otherwise, if its larger than the thing ont he minHeap AND ti came later theres no point in pushing it ontot he minheap since it cant ever be the min


        

    def pop(self) -> None:
        toremove = self.derStack.pop()
        if self.minHeap[0] == toremove:
            heapq.heappop(self.minHeap)


        

    def top(self) -> int:
        return self.derStack[-1]
        

    def getMin(self) -> int:
        return self.minHeap[0]
        
