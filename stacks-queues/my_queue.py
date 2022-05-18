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


    # def __str__(self):
    #     return 'data: ' + self.data + " -> next " + self.next.data if self.next != None else ""


class MyQueue:
    def __init__(self):
        self.front = self.rear = None

    def add(self, data: T):
        temp = Node(data)

        if self.front == None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp

        print(self.rear)
    

    def remove(self):
        if self.front == None:
            raise QueueEmptyError

        data = self.front.data
        self.front = self.front.next

        return data

    def peek(self):
        return self.first.data

    def is_empty(self):
        return self.front == None

my_queue = MyQueue()
my_queue.add("Thiago")
my_queue.add("Bruno")
my_queue.add("Melo")
my_queue.add("Sales")
print(my_queue.remove())
print(my_queue.remove())
print(my_queue.remove())