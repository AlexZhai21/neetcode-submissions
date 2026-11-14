class MinStack:

    def __init__(self):
        self.der_stack = []
        self.min_track = [] #stores the minimum element up to index i for ecah idnex


    def push(self, val: int) -> None:
        self.der_stack.append(val)
        if self.min_track:
            self.min_track.append(min(self.min_track[-1], val))
        else:
            self.min_track.append(val)
    def pop(self) -> None:
        self.der_stack.pop()
        self.min_track.pop()
        

    def top(self) -> int:
        return self.der_stack[-1]
        

    def getMin(self) -> int:
        return self.min_track[-1]
        
