from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window_size: int = size
        self.inputs: deque = deque()

    def next(self, val: int) -> float:
        self.inputs.append(val)
        if len(self.inputs) > self.window_size:
            self.inputs.popleft()  # O(1)
        return sum(self.inputs) / len(self.inputs)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
