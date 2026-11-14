class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        to_remove = []
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr in seen:
                to_remove.append(i)

            seen.add(curr)
        removed = 0
        for i in to_remove:
            nums.pop(i - removed)
            removed += 1 
        return len(seen)
        