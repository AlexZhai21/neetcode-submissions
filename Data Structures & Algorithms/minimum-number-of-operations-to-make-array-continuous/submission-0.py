class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        r = max(nums)
        ans = float('inf')
        n = len(nums)
        while l <= r:
            m = l + (r-l)//2 #the starting point
            ep = m + n #the ending point (non inclusive)
            # print(f"start {m}")
            # print(f"end {ep - 1}")
            inside = 0
            below = 0
            above = 0
            dups = 0
            seen = set()
            for i in nums:
                if i not in seen:
                    if i >= m and i < ep: #is within the range defiend by n
                        inside += 1
                    elif i < m:
                        below += 1
                    elif i >= ep:
                        above += 1
                else:
                    dups += 1
                seen.add(i)
            # print(below)
            # print(above)
            # print(inside)
            ans = min(ans, above + below + dups)
            if above > below: #more things are above this range than below it
                l = m + 1
            else:
                r = m - 1
        return ans


        