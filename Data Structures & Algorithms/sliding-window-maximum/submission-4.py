from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque([]) #this will be a deque of tuples of (number, index)
        
        l = 0
        r = 0
        while r < k:
            while dq and nums[r] > dq[-1][0]:
                dq.pop()
            dq.append((nums[r], r))
            r += 1
        ans.append(dq[0][0])
        l += 1
        if dq[0][1] < l: #if this index is no longer int he widnwo, we pop it
            dq.popleft()
        while r < len(nums):
            while dq and nums[r] > dq[-1][0]:
                dq.pop()
            dq.append((nums[r], r))
            ans.append(dq[0][0]) #this stores the largest we've seen in that current window
            l += 1
            if dq[0][1] < l: #if this index is no longer int he widnwo, we pop it
                dq.popleft()
            r += 1
        return ans