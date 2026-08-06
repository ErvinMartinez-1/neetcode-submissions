class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stck = []
        operands = ["+", "-", "*", "/"]

        for value in tokens:
            if value not in operands:
                stck.append(int(value))
            elif value == '+':
                stck.append(stck.pop() + stck.pop())
            elif value == '-':
                a, b = stck.pop(), stck.pop()
                stck.append(b - a)
            elif value == '*':
                stck.append(stck.pop() * stck.pop())
            elif value == '/':
                a, b = stck.pop(), stck.pop()
                stck.append(int(b / a))
        return stck[0]