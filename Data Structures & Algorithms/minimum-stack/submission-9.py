class MinStack:

    def __init__(self):
        self.stck = []
        self.minStck = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.minStck:
            self.minStck.append(val)
        else:
            self.minStck.append(min(val, self.minStck[-1]))

    def pop(self) -> None:
        if self.stck and self.minStck:
            self.stck.pop()
            self.minStck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minStck[-1]
