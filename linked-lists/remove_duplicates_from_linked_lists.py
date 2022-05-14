# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints: #9, #40

class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.next = None

    def __str__(self):
        return "Node[id = " + str(self.node_id) + "] - "

class LinkedList:
    def __init__(self, head):
        if head == None:
            self.head = Node(1)
        else:
            self.head = head

    def add(self, n: Node):
        if self.head.next == None:
            self.head.next = n
            return
        
        currentNode = self.head
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = n

    def get_n(self, n_element):
        current_node = self.head

        j = 0
        while(j < n_element or current_node == None):
            j = j + 1
            current_node = current_node.next

        return current_node

    def remove_duplicates_with_buffer(self):
        structure = {}

        current_node = self.head
        previous_node = self.head
        while (current_node != None):
            if current_node.node_id in structure:
                previous_node.next = current_node.next
            else:
                structure[current_node.node_id] = True
                previous_node = current_node
            
            current_node = current_node.next

        
    def __str__(self):
        content = self.head.__str__()

        current_node = self.head.next
        while current_node != None:
            print("passou 1")
            content += current_node.__str__()
            current_node = current_node.next

        return content

linkedList = LinkedList(Node(1))
# print(linkedList)
linkedList.add(Node(2))
linkedList.add(Node(3))
linkedList.add(Node(3))
linkedList.add(Node(4))
linkedList.add(Node(3))
linkedList.add(Node(4))
linkedList.add(Node(5))

print(linkedList)

linkedList.remove_duplicates_with_buffer()

print(linkedList)


# class Solution:
#     pass