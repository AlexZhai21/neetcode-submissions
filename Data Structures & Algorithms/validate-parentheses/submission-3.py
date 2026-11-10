class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        der_stack = []
        for i in s:
            if i in tracker:
                if der_stack and der_stack[-1] == tracker[i]:
                    der_stack.pop() #pop the most recently added open paranthesis to show that it is done
                    continue
                else:
                    return False
            else:
                der_stack.append(i)
        return not der_stack
        