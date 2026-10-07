class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: #what would make this current s2 window invalid?
    #1. if it contains a value not in s1
    # OR 2. if it is a value in s1 but the number of occurances of it is > than the one in s1
        s1_tracker = {}
        s2_tracker = {}
        l = 0 
        for s in s1:
            s1_tracker[s] = 1 + s1_tracker.get(s, 0)
        for r in range(len(s2)):
            s = s2[r]
            if s not in s1_tracker:
                l = r
                s2_tracker = {}
            elif s in s1_tracker:
                s2_tracker[s] = 1 + s2_tracker.get(s, 0)
                while s2_tracker[s] > s1_tracker[s]:
                    if s2[l] in s2_tracker:
                        s2_tracker[s2[l]] -= 1
                        if s2_tracker[s2[l]] == 0:
                            s2_tracker.pop(s2[l])
                    l += 1
            if s1_tracker == s2_tracker:
                return True
        return False













        # if len(s1) > len(s2):
        #     return False
        # for s in s1:
        #     s1_tracker[s] = 1 + s1_tracker.get(s, 0)
        # for r in range(len(s2)):
        #     if s2[r] in s1_tracker:
        #         s2_tracker[s2[r]] = 1 + s2_tracker.get(s2[r], 0)
        #         while s2_tracker[s2[r]] > s1_tracker[s2[r]]:
        #             s2_tracker[s2[l]] -= 1
                    
        #             if s2_tracker[s2[l]] == 0:
        #                 s2_tracker.pop(s2[l])
        #             l += 1
        #     else:
        #         if s2[l] in s2_tracker:
        #             s2_tracker[s2[l]] -= 1
        #             if s2_tracker[s2[l]] == 0:
        #                 s2_tracker.pop(s2[l])
        #         l += 1
        #     unequal_values = 0
        #     if len(s1_tracker) == len(s2_tracker):
        #         for s in s1_tracker:
        #             if s1_tracker[s] != s2_tracker[s]:
        #                 unequal_values += 1
        #         if unequal_values == 0:
        #             return True
        # return False
        
        