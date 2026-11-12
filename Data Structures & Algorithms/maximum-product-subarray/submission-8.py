class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #similar to max subarray, except you shoudl be dropping a prefix subarray when the product hits 0. since you cant ever get a better answer
        #you should be keepign the smallest possible product as well, sinec with negatives, the smallest product * a negative can now become the largest
        minProd = 1
        maxProd = 1
        ans = float('-inf')
        for i in nums:
       
    
            maxProd, minProd = max(i, maxProd * i, minProd * i), min(i, minProd * i, maxProd * i) #minProd * i could become the max if i is negative

  
            ans = max(ans, maxProd)
        return ans
        