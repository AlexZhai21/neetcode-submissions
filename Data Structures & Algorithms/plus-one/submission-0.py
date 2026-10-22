class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            curr_val = carry  + digits[i]
            print(f"{i}: {curr_val}")
            if curr_val >= 10:
                digits[i] = curr_val % 10
                carry = 1
            else:
                digits[i] = curr_val
                carry = 0
        if carry > 0:
            digits = [carry] + digits
        return digits


       
       