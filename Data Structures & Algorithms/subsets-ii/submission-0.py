class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seen = set()

        def subs(ss, i):
            if tuple(sorted(ss)) in seen:
                return
            if i >= n:
                ans.append(ss)
                seen.add(tuple(sorted(ss)))
                return
            subs(ss + [nums[i]], i + 1)
            subs(ss, i  + 1)
        
        subs([], 0)
        return ans
            