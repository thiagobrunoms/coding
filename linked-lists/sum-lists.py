#617 => 6 * 100 + 1 * 10 + 7
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5) . Thatis,617 + 295 .
# Output: 9 -) 1 -) 2. That is, 912.
# Hints: #7, #30, #71, #95, #109



#7 + 1 * 10 + 6 * 100 => 7 * 10^0 + 1 * 10^1 + 6 * 10^2 

class Node:
    def __init__(self, value: int):
        self.value = value
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

    def get_number(self):
        number = 0

        current_node = self.head
        count = 0
        while current_node != None:
            number += current_node.value * 10 ** count
            count += 1

            current_node = current_node.next

        return number

linked1 = LinkedList(Node(7))
linked1.add(Node(1))
linked1.add(Node(6))
print(linked1.get_number())

linked2 = LinkedList(Node(5))
linked2.add(Node(9))
linked2.add(Node(2))

print(linked2.get_number())

result = linked1.get_number() + linked2.get_number()
print(result)

    