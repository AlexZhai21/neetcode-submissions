class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        #if l < r, the array between l and r is not rotated
        while l <= r:
            m = l + (r-l)//2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target:
                
                return m
            print(nums[m])
            #after this, we know that l r and m do not have target
            if nums[l] < nums[r]: #array between l and r is sorted
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else: #this means l > r, meaning the array between l and r has been rotated
                if nums[m] > nums[l]: #m is part of the ascending portion
                    if target > nums[l] and target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else: #if nums[m] < nums[l] M is part of the right sorted portion so m to r is sorted
                    if target > nums[m] and target< nums[r]: #th means target CANNOT be part of the sorted portion from L to whateveris
                        l = m + 1
                    else: #this means target > nums[l], o if its in there its gonan be 4
                        r = m - 1
        return -1




            

        