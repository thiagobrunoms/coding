

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


class Solution():
    def sum_two_lists_as_numbers(self, head1: Node, head2: Node):
        if head1.next == None and head2.next == None:
            new_node: Node = Node(head1.value + head2.value)
            return new_node

        sum_node = self.sum_two_lists_as_numbers(
            head1.next if head1.next != None else head1, head2.next if head2.next != None else head2)

        head1.value = head1.value + head2.value
        head1.next = sum_node

        return head1

    def reverse(self, head):
        if head == None or head.next == None:
            return head

        reversed = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return reversed


linkedlist = MyLinkedList()
linkedlist.addAtTail(2)
linkedlist.addAtTail(5)
linkedlist.addAtTail(7)

linkedlist2 = MyLinkedList()
linkedlist2.addAtTail(1)
linkedlist2.addAtTail(2)
linkedlist2.addAtTail(2)

s = Solution()
sum_node = s.sum_two_lists_as_numbers(linkedlist.head, linkedlist2.head)
# sum_node = s.reverse(sum_node)

current = sum_node
while current != None:
    print(current.value)
    current = current.next
