class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node[id = " + str(self.value) + "] - "


class LinkedList:
    def __init__(self, head):
        if head == None:
            self.head = Node(1)
        else:
            self.head = head

    def push(self, n: Node):
        if self.head == None:
            self.head = n

        n.next = self.head
        self.head = n

    def add(self, n: Node):
        if self.head.next == None:
            self.head.next = n
            return

        currentNode = self.head
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = n

    def show(self):
        current: Node = self.head
        while current != None:
            print(current.value)
            current = current.next

class Solution:
    def merge_interactively(self, head1: Node, head2: Node) -> Node:
        dummy = Node(0)
        tail = dummy

        while head1 is not None and head2 is not None:
            if head1.value < head2.value:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        if head1 == None:
            tail.next = head2
        elif head2 == None:
            tail.next = head1

        return dummy.next

print('start 1')
n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n8 = Node(8)
n10 = Node(10)

print('start 1')
n0 = Node(0)
n2 = Node(2)
n5 = Node(5)
n7 = Node(7)
n9 = Node(9)
n11 = Node(11)

print('start ll 1')
linked_list = LinkedList(n1)
linked_list.add(n3)
linked_list.add(n4)
linked_list.add(n6)
linked_list.add(n8)
linked_list.add(n9)
linked_list.add(n10)

print('start ll 2')
linked_list2 = LinkedList(n0)
linked_list2.add(n2)
linked_list2.add(n5)
linked_list2.add(n7)
linked_list2.add(n11)

print('showing 1')
linked_list.show()

print('showing 2')
linked_list2.show()

s = Solution()
print('merging', )
merged_interactively = s.merge_interactively(linked_list.head, linked_list2.head)
print('merged_interactively ', merged_interactively)
mergedLinkedList = LinkedList(merged_interactively)
mergedLinkedList.show()
