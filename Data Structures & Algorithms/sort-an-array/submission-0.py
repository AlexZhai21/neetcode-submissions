class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort

        def merge_sort(l): #list
            if len(l) == 1:
                return l
            half = len(l) //2
            l1 = merge_sort(l[:half])
            l2 = merge_sort(l[half:])
            p1, p2 = 0,0
            ans = []
            while p1 < len(l1) and p2 < len(l2):
                if l1[p1] < l2[p2]:
                    ans.append(l1[p1])
                    p1 += 1
                else:
                    ans.append(l2[p2])
                    p2 += 1
            while p2 < len(l2):
                ans.append(l2[p2])
                p2 += 1
            while p1 < len(l1):
                ans.append(l1[p1])
                p1 += 1
            return ans
        return merge_sort(nums)




        