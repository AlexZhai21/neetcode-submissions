class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
    
        num_needed = k
        ans = []
        tracker = [[]] * n #1,.....n
        d_tracker = {}
        for j in nums:
            d_tracker[j] = d_tracker.get(j, 0) + 1
        for d in d_tracker:
            len_num = d_tracker[d]
            tracker[len_num-1] = tracker[len_num-1] + [d]
        for i in range(n-1, -1,-1):
        
            if num_needed == 0:
                return ans
            len_ans = len(tracker[i]) #number of elements that appear that many times (i)
            if len_ans == 0:
                continue
            if len_ans > num_needed:
                to_add = tracker[i][:num_needed]
                ans.extend(to_add)
                num_needed = 0
            else:
                ans.extend(tracker[i])
                num_needed -= len_ans
  
        return ans

        