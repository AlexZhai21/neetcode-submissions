class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: x[1])
    
        der_int = intervals[-1]
        dp = [0] * n
        dp[n-1] = 0 #you know that from the last thing you dont need to remove anything
        for i in range(n-2, -1, -1):
            curr= intervals[i]
            curr_s = curr[0]
            curr_e = curr[1]
            if curr_e > der_int[0]: #overlaps, since sorting by last eleemtn, remove whichever ones starting element extends back fruther. if equal, remove the one witht he 
                dp[i] = dp[i + 1] + 1
        
                if curr_s > der_int[0]: #old interval extends fruther, remove it
                    der_int = curr
            else:
                dp[i] = dp[i + 1]
                der_int = curr
            
        
                
        return dp[0]


        