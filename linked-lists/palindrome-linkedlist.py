# Palindrome: Implement a function to check if a linked list is a palindrome.
# Hints: #5, #13, #29, #61, #101

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

        self.stack = [self.head]

    def add(self, node: Node):
        self.stack.append(node)

        if self.head.next == None:
            self.head.next = node
            return
        
        currentNode = self.head
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = node


    def is_palindrome(self) -> bool:
        print("elements", self.stack)
        current_node = self.head
        
        index = len(self.stack)
        while current_node != None:
            value = current_node.value
            
            element = self.stack.pop()
            if value != element.value:
                return False

            current_node = current_node.next

        return True
        


s = LinkedList(Node(3))
s.add(Node(2))
s.add(Node(1))
s.add(Node(1))
s.add(Node(2))
s.add(Node(3))

result = s.is_palindrome()
print(result)