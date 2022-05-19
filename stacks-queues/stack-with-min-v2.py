# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Hints: #27, #59, #78 

#Solution 2: each node keeps the min value that was found when it was pushed to the stack. This requires many data to be kept if the number of nodes are big. 

from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T, current_min: T):
        self.value = value
        self.current_min = current_min
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None
        
    def push(self, value):
        if self.top == None:    
            self.top = Node(value, value)
            return

        current_min_value = value if value <= self.top.current_min else self.top.current_min
        node = Node(value, current_min_value)
        node.next = self.top
        self.top = node

    def pop(self):
        value = self.top.value
        self.top = self.top.next
        return value

    def min(self):
        return self.top.current_min


stack = MyStack()
stack.push(3)
stack.push(4)
stack.push(2)
stack.push(6)

print('poping', stack.pop())
print('poping', stack.pop())
print('poping', stack.pop())

print(stack.min())