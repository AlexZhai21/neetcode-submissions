class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float('inf')
        while l <= r:
            m = l + (r-l)//2
            #if left < right, do normal binary search:
            if nums[l] <= nums[r]:
                ans = min(nums[l], ans)
                return ans
            elif nums[l] > nums[r]: #been cycled 1 to n-1 times
                if nums[m] >= nums[l]: #you know from l to m is the second increasing side
                    l = m + 1
                elif nums[m] < nums[l]:
                    ans = min(nums[m], ans)
                    r = m-1
        return ans


        