class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0
        for i in nums:
            if not res:
                res = nums[0]
                count += 1
            elif i != res:
                count -= 1
                if count == -1:
                    res = i
                    count = 1
            elif i == res:
                count += 1
        return res