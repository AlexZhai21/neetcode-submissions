class Solution:
    def tribonacci(self, n: int) -> int:
        ans = 0
        tri_tracker = {}
        tri_tracker[0] = 0
        tri_tracker[1] = 1
        tri_tracker[2] = 1
        for i in range(3, n + 1):
            tri_tracker[i] = tri_tracker[i - 1] + tri_tracker[i-2] + tri_tracker[i-3]
        return tri_tracker[n]


        
        