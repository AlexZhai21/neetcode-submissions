import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        der_stack = []
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
        for t in tokens:
            if t not in ops:
                der_stack.append(t)
            else: #one of the opeators
                o2 = int(der_stack.pop())
                o1 = int(der_stack.pop())
                der_stack.append(ops[t](o1, o2))
        return int(der_stack[0])


        