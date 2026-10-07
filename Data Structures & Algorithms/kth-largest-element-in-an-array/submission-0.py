class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]










        #kth largest in the array means k -1 larger than it

        