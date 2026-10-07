class Solution:
    def numDecodings(self, s: str) -> int:
        #must be between 1, 26
        #go through
        tracker = {} #index to number of things
        def dp(f_s, s_s, step): #f_s is a list which contains each component so far, s_s is the ramining part of the string, step is either move forward by 1 or by 2
        #the reason we cant move forward by anyting else except 1 or 2 is that any 3 digit number is automatically invalid
            t_key_check = s_s + str(step)
            if t_key_check in tracker:
                return tracker[t_key_check]
            s_s_n = len(s_s)
            if s_s_n == 0: #finished grabbing everything
                
                return 1
            if step > s_s_n:
                return 0
            if s_s_n > 0 and s_s[0] == "0": #our reamining string created starts with a leading 0, invalid
                return 0
            temp_fs = f_s + [s_s[0: step]]
            temp_s_s = s_s[step:]
            if temp_fs and int(temp_fs[-1]) > 26: #if the thing we just added is too large of a number, then also invalid
                return 0
            ans = dp(temp_fs, temp_s_s, 1) + dp(temp_fs, temp_s_s, 2)
            t_key = s_s + str(step)
            tracker[t_key] = ans
            return ans
        ans = dp([], s,1) + dp([], s,2)
        return ans//2





        
        