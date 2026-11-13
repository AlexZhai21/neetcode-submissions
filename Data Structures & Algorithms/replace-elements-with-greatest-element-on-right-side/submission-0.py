class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suff_max = [-1]
        #suff_max[-1] contains the max so far
        n = len(arr)
        for i in range(n-1, 0, -1):
            curr_num = arr[i]
            if curr_num > suff_max[-1]:
                suff_max.append(curr_num)
            else:
                suff_max.append(suff_max[-1])
        #now we have to reverse the array
        p1 = 0
        p2 = n-1
        while p1 < p2:
            temp = suff_max[p1]
            suff_max[p1] = suff_max[p2]
            suff_max[p2] = temp
            p1 += 1
            p2 -= 1
        return suff_max

        