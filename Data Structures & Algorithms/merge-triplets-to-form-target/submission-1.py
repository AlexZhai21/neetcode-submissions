class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def de_func(trip1, trip2):
            to_return = [0] * 3
            for i in range(3):
                to_return[i] = max(trip1[i], trip2[i])
            return to_return
        ans = [float('-inf'), float('-inf'), float('-inf')]
        for t in triplets:
            for i in range(3):
                if t[i] == target[i]:
                    mistakes = 0
                    for j in range(3):
                        if j != i and t[j] > target[j]:
                            mistakes += 1
                    if not mistakes:
                        ans = de_func(ans, t)
        return ans == target
        
        
        