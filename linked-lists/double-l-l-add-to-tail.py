class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None
        self.previous: Node = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToStart(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head.previous = node
        self.head = node

    def addToEnd(self, node):
        if self.head == None:
            self.addToStart(node)
            return
        
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def showForward(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def showBackward(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.previous


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

list = DoubleLinkedList()
list.addToStart(n1)
list.addToStart(n2)
list.addToStart(n3)
list.addToStart(n4)
list.addToStart(n5)
list.showForward()
list.showBackward()
        
