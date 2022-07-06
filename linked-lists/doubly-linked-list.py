from locale import currency


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def push(self, value):
        new_node: Node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        current: Node = self.head
        while current.next != None:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def addAtIndex(self, value, index):
        current: Node = self.head

        for i in range(index):
            current = current.next

        new_node: Node = Node(value)
        new_node.previous = current.previous
        new_node.next = current
        current.previous.next = new_node
        current.previous = new_node

    def removeAtIndex(self, index):
        current: Node = self.head
        for i in range(index):
            current = current.next

        current.previous.next = current.next
        current.next.previous = current.previous

    def show(self):
        current: Node = self.head
        while current.next != None:
            print('Current value ', current.value)
            if current.previous != None:
                print('Previous value', current.previous.value)

            if current.next != None:
                print('Next value', current.next.value)

            current = current.next


dll = DoublyLinkedList()
dll.push(10)
dll.push(20)
dll.push(30)
dll.push(40)
dll.show()
print('==== AFTER INSERTING === ')
dll.addAtIndex(35, 2)
dll.show()

print('==== AFTER DELETING === ')
dll.removeAtIndex(2)
dll.show()
