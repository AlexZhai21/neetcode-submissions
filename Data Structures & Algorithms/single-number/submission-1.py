class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #a^a = 0
        #a^ 0 = a
        #bitwise operations are communititive, so a^b^c^a is the same as a^a^b^c, which is just 0^b^c 
        res = 0
        for i in nums:
            res = res ^ i
        return res
        