class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens == []: return 0
        stack = []
        for e in tokens:
            if e == '+' or e == '-' or e == '*' or e == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                r = 0
                if e == '+':
                    r = num1 + num2
                if e == '-':
                    r = num2 - num1
                if e == '*':
                    r = num1 * num2
                if e == '/':
                    r = int(num2 / num1)
                stack.append(str(r))
                # print(num2, num1, r)
            else:
                stack.append(e)

        return int(stack[0])