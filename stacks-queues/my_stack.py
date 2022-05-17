from locale import currency
from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self, top: Node):
        self.top = top

    def push(self, node: Node):
        #Bruno -> Thiago
        node.next = self.top
        self.top = node
        

    def pop(self):
        node = self.top
        self.top = self.top.next

        return node  

    def peek(self):
        return self.top.data

stack = MyStack(Node("Thiago"))
stack.push(Node("Bruno"))
stack.push(Node("Melo"))
stack.push(Node("Sales"))
print('top data', stack.peek())
print('poped', stack.pop().data)
print('poped', stack.pop().data)
print('poped', stack.pop().data)

print('top data', stack.peek())

