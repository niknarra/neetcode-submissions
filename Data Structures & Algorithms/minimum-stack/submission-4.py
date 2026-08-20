class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            currMin = self.stack[-1][1]
            if val < currMin:
                self.stack.append((val, val))
            else:
                self.stack.append((val, currMin))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
