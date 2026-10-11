class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        tracker = {}
        n3 = len(s3)
        n1 = len(s1)
        n2 = len(s2)

        def dp(i, j, k):#s1's index, s2's index
            #at each step, you can either take a letter from s1 or s2 and add it to the total
            #if s1[i] == s3[i] add s1 
            #if both are equal, probably wanna do the index thats smaller
            if k >= n3:
                return i >= n1 and j >= n2
                

            if i < n1 and j < n2 and s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            
            if (i, j, k) in tracker:
                return tracker[(i, j, k)]
            
            if (i < n1 and s1[i] == s3[k]) and (j < n2 and s2[j] == s3[k]):
                ans = dp(i + 1, j, k + 1) or dp(i, j + 1, k + 1)
            elif i < n1 and s1[i] == s3[k]:
                ans = dp(i + 1, j, k + 1)
            elif j < n2 and s2[j] == s3[k]:
                ans = dp(i, j + 1, k + 1)
            
            else:
                ans = False
            tracker[(i, j, k)] = ans
            return ans
        return dp(0,0,0)
        