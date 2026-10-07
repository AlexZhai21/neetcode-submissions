class TimeMap:

    def __init__(self):
        self.tracker = {} #name: list
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tracker:
            self.tracker[key] = []
        self.tracker[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tracker:
            return ""
       
        #otherwise, hit up binary search to find the largest element that is smaller than timestamp
        l = 0
        r = len(self.tracker[key]) - 1
        pot_ans = None
    
        while l <= r:
            m = l + (r-l)//2
        
            if timestamp > self.tracker[key][m][0]:
                pot_ans = m
            
                l = m + 1
            elif timestamp == self.tracker[key][m][0]:
                return self.tracker[key][m][1]
            else:
                r = m - 1
        if type(pot_ans) == int:
            return self.tracker[key][pot_ans][1]
        return ""


        

#[1: happy 2: ]