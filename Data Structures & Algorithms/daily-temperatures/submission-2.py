class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        der_stack = [] #the stack contains (the temp, the day)
        for i in range(n):
            der_temp = temperatures[i]
        
            while der_stack and der_temp > der_stack[-1][0]:
                days = i - der_stack[-1][1]
                result[der_stack[-1][1]] = days
                der_stack.pop()
            der_stack.append((der_temp, i))
        return result
        