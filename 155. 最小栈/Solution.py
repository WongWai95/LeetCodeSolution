class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min == [] or self.min[-1] >= x:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack == []:
            return
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min == []:
            return None
        else:
            return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()