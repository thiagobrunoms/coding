

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def remove_nth_element(self, n: int):
        slow = self.head
        fast = self.head

        for i in range(n+1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        self.show()


linkedlist = MyLinkedList()
linkedlist.addAtHead(10)
print('== SHOW == ')
linkedlist.show()
linkedlist.addAtTail(20)
linkedlist.addAtTail(30)
linkedlist.addAtTail(40)
linkedlist.addAtTail(50)
linkedlist.addAtTail(60)
linkedlist.addAtTail(70)
print('== SHOW == ')
linkedlist.show()

print('=== removing nth ======')
linkedlist.remove_nth_element(6)
