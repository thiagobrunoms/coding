class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, initial: int):
        self.head = Node(initial)

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

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
    
    def reverse(self):
        self.head = self.reverse_myself(self.head)
    
    def reverse_myself(self, node: Node):
        if (node == None):
            return node

        if (node.next == None):
            return node

        node1 = self.reverse_myself(node.next)
        node.next.next = node
        node.next = None
        return node1
    
    def is_empty(self):
        return self.head == None

    def show(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


print("Current List === ")
linkedList = LinkedList(0)
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)
linkedList.show()

print('reversing the linked list')
linkedList.reverse()
linkedList.show()

#The sequence of removal assert checks depends if the list is reversed or not - pay attention!
print("Popping === ")
if not linkedList.is_empty():
    popped = linkedList.pop()
    assert popped.data == 0, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 1, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 2, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 3, 'Failed'

    print("Current List === ")
    is_empty = linkedList.is_empty()
    assert is_empty, 'Faild - not empty'
