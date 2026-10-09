class MinStack:

    def __init__(self):
        self.elements = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        val = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)
        

    def pop(self) -> None:
        self.elements.pop()
        self.minimum.pop()


    def top(self) -> int:
        # gets the top element.
        return self.elements[-1]

    def getMin(self) -> int:
        # gets the smallest element, which is at the top of minimum.
        return self.minimum[-1]
