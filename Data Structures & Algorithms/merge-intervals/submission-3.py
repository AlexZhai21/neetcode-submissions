class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #sorts by the starting value
        n = len(intervals)
        print(intervals)
        ans = []
        new_int = []
        for i in range(n):
            if new_int:
                curr_int = new_int
            else:
                curr_int = intervals[i]
            if i < n-1:
                next_int = intervals[i + 1]
                if curr_int[-1] >= next_int[0]: #overlapping
                    if new_int:
                        new_int_start = new_int[0]
                        new_int_end = new_int[-1]
                    else:
                        new_int_start = float('inf')
                        new_int_end = float('-inf')
                    new_int = [min(new_int_start, curr_int[0]), max(curr_int[-1], next_int[-1], new_int_end)]
                else:
        
                    #not overlapping
                    if new_int:
                        ans.append(new_int)
                    else:
                        ans.append(curr_int)
                
                    new_int = [] #reset the new_int
            else:
                if new_int:
                    ans.append(new_int)
                else:
                    ans.append(curr_int)
        return ans



        