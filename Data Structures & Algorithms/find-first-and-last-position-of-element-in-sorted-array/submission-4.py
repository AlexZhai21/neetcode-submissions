class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch(l, r, leftBias):
            while l <= r:
                m = l + (r - l) //2
                if nums[m] > target:
                    return binsearch(l, m-1, leftBias)
                elif nums[m] < target:
                    return binsearch(m + 1, r, leftBias)
                else: #this means nums[m] is equal to target
                    if leftBias:
                        self.left = m
                        return binsearch(l = l, r = m - 1, leftBias = True)
                    else:
                        self.right = m
                        return binsearch(l = m + 1, r = r, leftBias = False)
            return -1
        self.left = -1
        self.right = -1
        binsearch(0, len(nums) -1, True)
        binsearch(0, len(nums) -1, False)
        return [self.left, self.right]
        # first_found = binsearch(l = 0, r = len(nums) - 1, exist = None)
        # if first_found[0] or first_found[0] == 0: 
        #     left = binsearch(l = first_found[1], r = first_found[0] - 1, exist = first_found[0])[0]
        #     right = binsearch(l = first_found[0] + 1, r = first_found[2], exist = first_found[0])[0]
        # else:
        #     left = -1
        #     right = -1
 
        # return [left, right]

