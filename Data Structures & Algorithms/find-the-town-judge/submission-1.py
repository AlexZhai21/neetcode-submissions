class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tracker = {}
        ans = -1
        for i in range(1, n + 1):
            tracker[i] = set()
        for e in trust:
            tracker[e[0]].add(e[1])
        for i in tracker:
            num_trust = 0
            if len(tracker[i]) == 0: #this is potentialy the town judge
                for j in tracker:
                    if i == j:
                        continue
                    else:
                        if i in tracker[j]:
                            num_trust += 1
                if num_trust == n - 1:
                    ans = i
                    return ans
            
        return ans


        #1 -> 3
        # 4 -> 3
        #2 -> 3