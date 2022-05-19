# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Hints: #27, #59, #78 

#Solution 1: uses two stacks. The main advantage of such a solution is that if the min value is one of the first values e many of others, a second stack would use few space (O(1)?)

from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
        self.min_top = None
    
    def push(self, value: T):
        node = Node(value)
        node.next = self.top
        self.top = node

        if self.min_top == None:
            self.min_top = Node(value)
            return
        
        if value < self.min_top.value:
            min_node = Node(value)
            min_node.next = self.min_top
            self.min_top = min_node

    def pop(self):
        value = self.top.value
        self.top = self.top.next

        if value == self.min_top.value:
                 self.min_top = self.min_top.next

        return value

    def min(self):
        return self.min_top.value


stack = MyStack()
stack.push(3)
stack.push(4)
stack.push(2)
stack.push(6)

print('poping', stack.pop())
print('poping', stack.pop())

print(stack.min())
