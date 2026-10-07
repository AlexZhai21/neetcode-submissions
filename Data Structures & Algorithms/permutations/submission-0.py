class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtracker(path, index):
            if index >= len(nums):
                self.ans.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if path[i] != None:
                    continue
                path[i] = nums[index]
                backtracker(path, index + 1)
                path[i] = None
                
                

        backtracker([None] * len(nums), 0)
        return self.ans

            

