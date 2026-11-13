class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        tracker = [[] for i in range(n)]
        amt = {}
        for z in nums:
            amt[z] = amt.get(z, 0) + 1

        for a in amt:
            tracker[amt[a] - 1].append(a)
        k_left = k
    
        ans = []
        for i in range(n-1, -1, -1):
            for j in tracker[i]:
             
                ans.append(j)
                print(j)
                k_left -= 1
                print(k_left)
                if k_left <= 0:
                    return ans
                



        