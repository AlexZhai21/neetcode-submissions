class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bin_search(l, r, leftBias):
            ans = -1
            while l <= r:
                m = l + (r-l) //2
                if nums[m] > target: #target if in array is on the left side
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    #now you found target, but is it the best one or not?
                    ans = m # found
                    if leftBias:
                        #want to find the left most
                        r = m - 1
                    else:
                        l = m + 1

            return ans
        left = bin_search(0, len(nums) - 1, True)
        right = bin_search(0, len(nums) -1, False)
        return [left, right]

