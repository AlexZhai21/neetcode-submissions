class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #returns true if within k + 1 numbers thers a duplicate
        seen = set() 
        l = 0
        for r in range(len(nums)):
            while r - l > k: #widnow size too big, this keeps seen at only k + 1 or less
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
        return False

            



                
            


            
            
        