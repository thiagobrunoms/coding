class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def push(self, data: int):
        self.length = self.length + 1
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def add(self, data: int):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        current = self.head
        while current.next != None:
            current = current.next

        current.next = node
        self.length = self.length + 1

    def insert(self, data: int, index: int):
        if index > self.length + 1:
            raise Exception('index biggest than linked list length: ' + str(self.length))
        
        self.length = self.length + 1
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        if index == 0: #can reuse the 'push' method
            node.next = self.head
            self.head = node
            return

        position = 0
        current = self.head
        while (position + 1 < index):
            current = current.next
            position = position + 1

        node.next = current.next
        current.next = node
        
    def pop(self):
        if self.head == None:
            return
        
        self.length = self.length - 1
        if self.head.next == None:
            temp = self.head
            self.head = None
            return temp
        
        temp = self.head
        self.head = self.head.next
        return temp
    
    def delete_at(self, index):
        if index > self.length:
            raise Exception('Element does not exist!')
        
        if index == 0:
            self.pop()
            return
    
        position = 0
        previous = self.head
        current = self.head
        while position < index and current.next != None: # 1->2->3->4
            previous = current
            current = current.next
            position = position + 1

        previous.next = current.next
        self.length = self.length - 1
    
    def reverse(self, recursively: bool):
        if recursively:
            self.head = self.__reverse_myself(self.head)
        else:
            self.__reverse_iteratively()
    
    def __reverse_iteratively(self):
        previous: Node = None
        current = self.head
        
        while current != None:
            nextNode = current.next          
            current.next = previous
            previous = current
            current = nextNode
            
        self.head = previous

    def __reverse_myself(self, node: Node):
        if (node == None):
            return node

        if (node.next == None):
            return node

        node1 = self.__reverse_myself(node.next)
        node.next.next = node
        node.next = None
        return node1
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def is_empty(self):
        return self.head == None

    def show(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def check(self):
        first = self.head
        print(first.data)
        second = first.next
        print(second.data)
        third = second.next
        print(third.data)
        fourth = third.next
        print(fourth.data)
        fifth = fourth.next
        print(fifth.data)


print("Current List === ")
linkedList = LinkedList()
linkedList.push(0)
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
linkedList.show()

print('reversing the linked list')
linkedList.reverse(True)
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

print("new list")
ll2 = LinkedList()
ll2.insert(0, 0)
ll2.show()

try:
    ll2.insert(11, 100)
except Exception as e:
    print(e)

ll3 = LinkedList()
ll3.add(0)
ll3.add(1)
ll3.add(2)
ll3.add(3)
ll3.add(4)
ll3.insert(100, 4)
ll3.show()
ll3.insert(150, 5)
ll3.show()

ll3.insert(200, 6)
ll3.show()

ll3.insert(300, 3)
ll3.show()

print('after removing first')
ll3.delete_at(0)
ll3.show()
print('after removing last')
ll3.delete_at(ll3.length)
ll3.show()

print('Reverting interactively')
ll3.reverse(False)
ll3.show()

print('Middle node')
middle = ll3.find_middle_node()
print(middle.data)
