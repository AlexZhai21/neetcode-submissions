class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        num_jobs = len(jobDifficulty)
        tracker = {}
        if num_jobs < d:
            return -1
        def dp(i, days, curr_max): #minimum difficulty of a job schedule from jobDiffulcty[i:] and days number of days left
            if (i, days, curr_max) in tracker:
                return tracker[(i, days, curr_max)]
            if i == num_jobs and days < d: #some days dont have jobs
                return float('inf')
            if i == num_jobs and days == d: #all days have jobs
                return curr_max # for the last max
            if i < num_jobs and days == d: #all the reamining jobs msut be in the last day
                return max(curr_max, max(jobDifficulty[i:]))
            
           
            #if stay ont he same day, the new curr_max is this:
            new_max = max(curr_max, jobDifficulty[i])
            if i > 0:
           
           
                ans = min(dp(i + 1, days, new_max), curr_max + dp(i + 1, days + 1, jobDifficulty[i]))
            else:
                ans = dp(i + 1, days, new_max)
            #can either include this job as part of the same day (i + 1, days) or this job is for the next day (i + 1, day + 1, difficulty of i)
            #same day: max()
            tracker[(i, days, curr_max)] = ans
            return ans
        res = dp(0,1,jobDifficulty[0])
 
        if res == float('inf'):
            return -1
        return res

            
