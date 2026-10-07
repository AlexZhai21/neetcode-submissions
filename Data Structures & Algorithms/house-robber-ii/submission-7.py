class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(num):
            n = len(num)
            if n < 2:
                return max(num)
            
            tracker = {}
            tracker[n] = 0
            tracker[n - 1] = num[-1]
            tracker[n -2] = num[-2]
            for i in range(n-3, -1, -1):
                curr_ans = num[i]
                curr_ans += max(tracker[i + 2], tracker[i + 3])
                tracker[i] = curr_ans
            return max(tracker[0], tracker[1])
        if len(nums) <= 1:
            return max(nums)

        ans = max(robber(nums[:-1]), robber(nums[1:]))
        return ans


        # n = len(nums)
        # if n < 2:
        #     return max(nums)
        # ans = max(nums[-1], nums[-2])
        # last_house = nums[-1]
        # tracker = {} #need some way to track if it contains the last item or not
        # tracker[n] = (0, 0)
        # tracker[n - 1] = (nums[-1], 1) #the 1 indicats this includes the last item
        # tracker[n -2] = (nums[-2], 0)
        # for i in range(n-3, -1, -1):
        #     curr_ans = 0
        #     i_2 = tracker[i + 2]
        #     i_3 = tracker[i + 3]
        #     i_2_val = i_2[0]
        #     i_3_val = i_3[0]
        #     includes_last = 0
        #     if i == 0: #this means we reached the first one and cant include 
        #         if i_2[1] == 1: #this means it includes the alst hign:
        #             i_2_val -= last_house
                
        #         if i_3[1] == 1:
        #             i_3_val -= last_house
                
        #     i_max_val = max(i_2_val, i_3_val)
    
        #     if (i_max_val == i_2_val and i_2[1] == 1) or (i_max_val == i_3_val and i_3[1] == 1):
        #         if i_2_val != i_3_val:
        #             includes_last = 1
        #         else:
        #             includes_last = 0

        #     curr_ans = nums[i] + i_max_val
        #     ans = max(ans, curr_ans)
        #     tracker[i] = (curr_ans, includes_last)
            
        # print(tracker)
        # return ans

            
                




        # #[6, 2, 9, 8 , 3, 6]
        # #[-1, 0, 1, 2, 3, 4]
        
        