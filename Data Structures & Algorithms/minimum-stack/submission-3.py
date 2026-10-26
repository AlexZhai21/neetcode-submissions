class MinStack:

    def __init__(self):
        self.mintracker = [] #tracks the minimum so far at the current idnex pushed
        self.derStack = []
        self.currmin = float('inf')
    def push(self, val: int) -> None:
        self.derStack.append(val)
        if val < self.currmin: #new min so far
            self.currmin = val
        self.mintracker.append(self.currmin)

    def pop(self) -> None:
        toremove = self.derStack.pop()
        removed_min = self.mintracker.pop()
        if not self.mintracker:
            self.currmin = float('inf')
        elif self.currmin == removed_min and self.mintracker[-1] > removed_min:
            self.currmin = self.mintracker[-1] #if youve poppped aay allt he current mins, then you wanna remove this one too
    def top(self) -> int:
        return self.derStack[-1]
        

    def getMin(self) -> int:
        return self.mintracker[-1]
        
