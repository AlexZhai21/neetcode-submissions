class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtracker(index, path):
            if index == len(nums):
                self.ans.append(path[:])
                return
            path.append(nums[index])
            backtracker(index + 1, path)
            path.pop()
            backtracker(index + 1, path)
        
        backtracker(0, [])
        return self.ans

            

        