class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        trip_seen = set()
        ans = []
        
        nums.sort()
        for i in range(len(nums)):
        
            n = nums[i]
            if n in seen:
                continue
            else:
                seen.add(n)
            l = i + 1
            r = len(nums) - 1
            look_for = 0 - n
            while l < r:
                l_n = nums[l]
                r_n = nums[r]
                d_sum = l_n + r_n
                if d_sum > look_for:
                    r -= 1
                elif d_sum < look_for:
                    l += 1
                else:
                    to_add = [n, l_n, r_n]
                    if tuple(to_add) not in trip_seen:
                        ans.append(to_add)
                    trip_seen.add(tuple(to_add))
                    l += 1
                    r -= 1

        return ans

                


        