class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        ans = []
        for s in strs:
            if "".join(sorted(s)) in tracker:
                tracker["".join(sorted(s))].append(s)
            else:
                tracker["".join(sorted(s))] = [s]
        for t in tracker:
            ans.append(tracker[t])
        return ans
        