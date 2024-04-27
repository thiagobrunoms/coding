class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data: int):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def add(self, data: int):
        node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next

        current.next = node

    def insert(self, data: int, index: int):
        position = 0
        current = self.head
        while (position + 1 < index):
            current = current.next
            position = position + 1

        node = Node(data)
        node.next = current.next
        current.next = node
        
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
        self.head = self.__reverse_myself(self.head)
    
    def __reverse_myself(self, node: Node):
        if (node == None):
            return node

        if (node.next == None):
            return node

        node1 = self.__reverse_myself(node.next)
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
linkedList = LinkedList()
linkedList.push(0)
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
linkedList.show()

print('reversing the linked list')
linkedList.reverse()
linkedList.show()

print('adding elements into the end of the linked list')
linkedList.add(4)
linkedList.add(5)
linkedList.show()

print('inserting at position 2')
linkedList.insert(100, 2)
linkedList.show()

#The sequence of removal assert checks depends if the list is reversed or not - pay attention!
print("Popping === ")
if not linkedList.is_empty():
    popped = linkedList.pop()
    assert popped.data == 0, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 1, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 100, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 2, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 3, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 4, 'Failed'

    popped = linkedList.pop()
    assert popped.data == 5, 'Failed'

    print("Current List === ")
    is_empty = linkedList.is_empty()
    assert is_empty, 'Faild - not empty'
