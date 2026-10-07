class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.ans = []
        def backtracker(index, path, total):
            if total == target:
                self.ans.append(path[:])
                return
            if index >= len(candidates) or total > target:
                return
            path.append(candidates[index])
            backtracker(index + 1, path, total + candidates[index])
            path.pop()
            i = index
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracker(i + 1, path, total)
        backtracker(0, [], 0)
        return self.ans
            
            

        