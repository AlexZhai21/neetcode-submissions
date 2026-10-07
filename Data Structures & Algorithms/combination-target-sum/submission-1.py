class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def backtracker(index, path):
            if sum(path) == target:
                self.ans.append(path[:])
                return
            elif index == len(nums) or sum(path) > target:
                return
            path.append(nums[index])
            backtracker(index, path)
            path.pop()
            backtracker(index + 1, path)
        backtracker(0, [])
        return self.ans
        