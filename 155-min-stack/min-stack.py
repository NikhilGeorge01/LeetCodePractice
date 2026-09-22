class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.minst:
            self.minst.append(value)
        elif value <= self.minst[-1]:
            self.minst.append(value)
    def pop(self) -> None:
        a = self.st.pop()
        if self.minst[-1] == a:
            self.minst.pop()
        return a
    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int:
        return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()