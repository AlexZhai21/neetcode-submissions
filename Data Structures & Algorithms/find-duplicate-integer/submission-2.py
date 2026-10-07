class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while fast != slow or fast == 0 and slow == 0: #0 cannot be in a cycle since nothing can point to 0
            slow = nums[slow]
            fast = nums[nums[fast]]
        #after this loop ends, slow == fast
        slow2 = 0
        while slow !=slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow


        # #O(n) space solution
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen.add(i)
        
        