"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

"""
import math


class MinStack:
    def __init__(self):
        self.min = math.inf
        self.prev_min = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.prev_min.append(self.min)
        if val <= self.min:
            self.min = val
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.min = self.prev_min[-1]
        self.prev_min.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return int(self.min)


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
