class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #lengthof the substring using a start and end pointer would be end - start + 1
        curr = 0
        ans = 0
        last_dup = -1 #this is the earliest index f
        tracker = {} #will trac the letter and index you most recently saw it.
        while curr < len(s):
            curr_letter = s[curr]
            if curr_letter in tracker: #this means we've seen this letter in the substring before
                ans = max(ans, curr - max(last_dup, tracker[curr_letter]))
                last_dup = max(tracker[curr_letter], last_dup) #we need it to be the max because we know that after the old last_dup, theres no duplicates, but before it, there is (which is why its the last dup)
                tracker[curr_letter] = curr
            
            else: #this means this letter has never been seen before
                tracker[curr_letter] = curr
                ans = max(ans, curr - last_dup)
            curr +=1

        return ans
        