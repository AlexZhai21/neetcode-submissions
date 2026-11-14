class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        offsets = {} #number: index
        for i in range(n):
            num = nums[i]
            if num in offsets:
                offsets[num].append((i + k)%n)
            else:
                offsets[num] = [(i + k)%n]
        for o in offsets:
            for j in offsets[o]:
                nums[j] = o
        