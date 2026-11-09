from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        m = n-k #max number of digits after we are done
        if m == 0:
            return "0"
        #1239 
        #9321 
        der_stack = deque([])
        k_rem = k
        for i in num:
            while der_stack and i < der_stack[-1] and k_rem > 0:
                der_stack.pop()
                k_rem -= 1
            der_stack.append(i)
        while k_rem > 0:
            der_stack.pop()
            k_rem -= 1
        # print(der_stack)
        while der_stack and der_stack[0] == "0":
            der_stack.popleft()
        # print(der_stack)
        if der_stack:
            return "".join(der_stack)
        return "0"
            

