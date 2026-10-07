class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved = []
        curr_ans = []
        for i in range(len(temperatures)):
            curr_ans.append(0)
        
        for i in range(len(temperatures)):
            while unresolved and temperatures[i] > temperatures[unresolved[-1]]:
                curr_ans[unresolved[-1]] = i - unresolved[-1] 
                unresolved.pop()
            unresolved.append(i)
        return curr_ans
            
            
            
            

        