class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        s_nums = set(nums)
        seen = set()
        start = {}
        end = {}
        s_subsets = []
        for n in nums: #this loop is o(n) time, seen make sure you hit everything only once
            curr_subset = [n]
            if n in seen:
                continue
            seen.add(n)
            look_for = n + 1
            while look_for in s_nums:
                seen.add(look_for)
                curr_subset.append(look_for)
                look_for += 1
            s_subsets.append(curr_subset)
            start[n] = len(curr_subset)
            end[look_for - 1] = len(curr_subset)
        for s in s_subsets:
            s_s = s[0]
            s_e = s[-1]
            if s_s in start and s_e in end:
                curr_ans = start[s_s]
                if s_s -1 in end: #you have a subarray ending in the start value - 1, meaning these 2 are consequctive
                    new_len = end[s_s - 1]
                    new_start = s_s - 1 - new_len + 1
                    start[new_start] += start[s_s]
                    start.pop(s_s)
                    end[s_e] += end[s_s -1]
                    end.pop(s_s - 1)
                    curr_ans += end[s_s - 1]
                    #end[s_s - 1] is the length of the subarray so we can get the start value from here            
                if s_e + 1 in start: #this means theres another subarray that starts with what we need to end with
                    new_len = start[s_e + 1]
                    new_end = s_e + new_len 
                    start[s_s] += start[s_e + 1]
                    start.pop(s_e + 1)
                    end[new_end] += end[s_e]
                    end.pop(s_e)
                    curr_ans += start[s_e + 1]
                ans = max(ans, curr_ans)
        return ans

        
            #start of this subset is n, so you awnt to look for other subsets ENDING
            #in start - 1
            #dend of this sbuset is look_for - 1, so you want to find other subsets STARTING in look_for
            ##MERGE STEP
            #start: {2: [2,3,4,5]}

            #end: {5: [2,3,4,5]}

