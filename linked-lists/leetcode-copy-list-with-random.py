

class Node:
    def __init__(self, value, next, random):
        self.value = value
        self.next = next
        self.random = random


class MyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.head == None:
            return None

        if index > self.size or index < 0:
            return None

        if index == 0:
            return self.head

        count = 1
        current: Node = self.head.next
        while current != None:
            if index == count:
                return current

            current = current.next
            count += 1

    def addAtHead(self, val: int) -> None:
        current: Node = Node(val)
        current.next = self.head
        self.head = current
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.size += 1
            return

        current: Node = self.head
        while current.next != None:
            current = current.next

        current.next = Node(val)
        # current.random =
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None

        if index == 0:
            self.addAtHead(val)
            return

        count = 0
        current: Node = self.head
        previous: Node = self.head
        while True:
            if count == index:
                new_node: Node = Node(val)
                previous.next = new_node
                new_node.next = current
                self.size += 1
                return

            count += 1
            previous = current
            current = current.next

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0 or index < 0 or index > self.size:
            return

        if index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next

            self.size -= 1
            return

        count = 0
        current: Node = self.head
        previous: Node = self.head
        while True:
            if count == index:
                previous.next = current.next
                self.size -= 1
                return

            count += 1
            previous = current
            current = current.next

    def show(self):
        current: Node = self.head
        while current != None:
            print(current.value)
            current = current.next


class Solution:
    # Needs more tests
    def copy(self, head: Node) -> Node:
        new_head: Node = Node(head.value, head.current, head.random)
        current: Node = head.next

        while current != None:
            temp: Node = Node(current.value, current.next, current.random)
            new_head.next = temp
            new_head = new_head.next
            current = current.next


linkedlist1 = MyLinkedList()
linkedlist1.addAtTail(10)
linkedlist1.addAtTail(20)
linkedlist1.addAtTail(30)
linkedlist1.addAtTail(40)
