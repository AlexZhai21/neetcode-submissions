class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
 
        tracker = {} #letter: num_times seen that letter
        ans = 0
        l = 0
        com_s = s[0] #com_s is the one we don't convert
        curr_len = 0
        #curr_len - tracker[com_s] = how many other letters we gotta convert
        for r in range(len(s)):
            curr_len += 1
            if s[r] in tracker: #this means curr letter is part of our substring
                tracker[s[r]] += 1
                if tracker[com_s] < tracker[s[r]]:
                    com_s = s[r]
            else:
                tracker[s[r]] = 1
            while curr_len - tracker[com_s] > k: #current substring has too many other shit to be converted to continious using k transformations
                tracker[s[l]] -= 1
                l += 1
                curr_len -= 1
                
                com_s = max(tracker, key=tracker.get)


            ans = max(ans, curr_len)
        return ans


        