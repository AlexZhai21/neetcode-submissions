class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        ans = []
        for s in strs:
            tracker["".join(sorted(s))] = tracker.get("".join(sorted(s)), []) + [s]
        for i in tracker:
            ans.append(tracker[i])
        return ans

        