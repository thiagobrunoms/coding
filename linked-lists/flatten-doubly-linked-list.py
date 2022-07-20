class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
        self.child = None


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

    # STILL NOT WORKING
    def flatten_doubly_linkd_list(self, head: Node):
        if head.child == None:
            if head.next == None:
                return head
            else:
                print(head.value)
                self.flatten_doubly_linkd_list(head.next)
        else:
            print(head.value)
            self.flatten_doubly_linkd_list(head.child)

        if head.next != None:
            print(head.value)
            self.flatten_doubly_linkd_list(head.next)

    # STILL NOT WORKING
    def flatten_doubly_linkd_list_v2(self, head: Node):
        if head.child != None:
            self.flatten_doubly_linkd_list_v2(head.child)

        if head.next != None:
            self.flatten_doubly_linkd_list_v2(head.next)

        return head


dll = DoublyLinkedList()
dll.push(10)
dll.push(20)
dll.push(30)
dll.push(40)
dll.show()
