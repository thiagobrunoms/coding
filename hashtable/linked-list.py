from locale import currency
from os import link


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.size = 0

    def insert(self, node: Node):
        if (self.head == None):
            self.head = node
            self.size += 1
            return

        node.next = self.head
        self.head = node
        self.size += 1

    def insertAt(self, index: int, node: Node) -> bool:
        print('insert at', index)
        if index == 0:
            self.insert(node)
            self.size += 1
            return True

        current = self.head
        previous = None

        count = 1
        while current != None:
            if count == index:
                node.next = current
                previous.next = node
                self.size += 1
                return True

            previous = current
            current = current.next
            count += 1

        return False

    def delete(self, position: int) -> bool:
        if position > self.size or position < 0:
            return False

        if position == 0:
            self.head = self.head.next

        current = self.head
        previous = None
        count = 1
        while count < self.size:
            if position == count:
                previous.next = current.next

            previous = current
            current = current.next
            count += 1

    def show(self):
        current = self.head
        while (current != None):
            print(current.value)
            current = current.next


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(25)

linkedList = LinkedList(n1)
linkedList.insert(n2)
linkedList.insert(n3)
linkedList.insert(n4)
linkedList.show()
print('=====')
linkedList.insertAt(2, n5)
linkedList.show()
print('=====')
linkedList.delete(2)
linkedList.show()
