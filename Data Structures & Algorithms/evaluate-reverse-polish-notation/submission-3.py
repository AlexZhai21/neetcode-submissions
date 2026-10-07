import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        curr_two = []
    
        for n in tokens:
            if n not in operations: #this means n is a number
                curr_two.append(int(n))
            elif n in operations:
                curr_ans = int(operations[n](curr_two[-2], curr_two[-1]))
                curr_two.pop()
                curr_two.pop()
            
                curr_two.append(curr_ans)
        print(curr_two)
        return curr_two[-1]





        