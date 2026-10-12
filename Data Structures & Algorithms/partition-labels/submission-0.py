class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        tracker = {}
        ans = []
        for i in s:
            tracker[i] = tracker.get(i, 0) + 1
        seen = set()
        curr_amt = 0
        der_key = None
        for i in s:
            if not der_key:
                der_key = i
    
            if i not in seen and i != der_key:
                tracker[der_key] += tracker[i]
                seen.add(i)
            tracker[der_key] -= 1
            curr_amt += 1
            if tracker[der_key] == 0:
                ans.append(curr_amt)
                curr_amt = 0
                der_key = None
        
        return ans

            
        

        