class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head_value):
        self.head = Node(head_value)

    def push(self, data):
        node = Node(data)
        node.data = data
        node.next = self.head
        self.head = node

    def reverse(self, node: Node):
        if (node == None):
            return node

        if (node.next == None):
            return node

        node1 = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return node1

    def pop(self):
        if self.head == None:
            return

        if self.head.next == None:
            temp = self.head
            self.head = None
            return temp

        temp = self.head
        self.head = self.head.next

        return temp

    def show(self):
        current = self.head

        while (current != None):
            print(current.data)
            current = current.next


linkedList = LinkedList(5)
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)

result = linkedList.reverse(linkedList.head)

current = result
while (current != None):
    print(current.data)
    current = current.next
# linkedList.show()

# poped = linkedList.pop()
# print('removed', poped.data)

# poped = linkedList.pop()
# print('removed', poped.data)

# poped = linkedList.pop()
# print('removed', poped.data)

# poped = linkedList.pop()
# print('removed', poped.data)
