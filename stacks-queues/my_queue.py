from typing import TypeVar, Generic

class Error(Exception):
    pass

class QueueEmptyError(Exception):
    pass


T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self, first: Node):
        self.first = first

    def add(self, node: Node):
        if self.first == None:
            self.first = node

        current_node = self.first
        while current_node.next != None:
            current_node = current_node.next 

        current_node.next = node

    def remove(self):
        if self.first == None:
            raise QueueEmptyError

        data = self.first.data
        self.first = self.first.next

        return data

    def peek(self):
        return self.first.data

my_queue = MyQueue(Node("Thiago"))
my_queue.add(Node("Bruno"))
my_queue.add(Node("Melo"))
my_queue.add(Node("Sales"))

print(my_queue.remove())
print(my_queue.remove())
print(my_queue.remove())
print(my_queue.remove())
try:
    print(my_queue.remove())
except QueueEmptyError:
    print('Não há elementos!')
