

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.last = head

    def append(self, node: Node):
        if self.head == None:
            self.head = node
            self.last = node
            return

        node.next = self.head
        self.last.next = node
        self.head = node

    def show(self):
        current = self.head
        while current != self.last:
            print(current.value)
            current = current.next

        print('last', current.value)


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

c = CircularLinkedList()
c.append(n1)
c.append(n2)
c.append(n3)
c.append(n4)
c.append(n5)
c.show()
