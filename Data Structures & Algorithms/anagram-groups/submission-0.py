class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        tracker = {}
        for s in strs:
            key_s = "".join(sorted(s))
 
            tracker[key_s] = [s] + tracker.get(key_s, [])
        for key_s in tracker:
            ans.append(tracker[key_s])
        return ans
    


        