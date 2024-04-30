class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node[id = " + str(self.node_id) + "] - "

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node: Node):
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def reverse(self):
        previous: Node = None
        current = self.head
        next: Node = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def show(self):
        current = self.head
        number = 0
        index = 0
        while current != None:
            number = number + (current.value * (10 ** index))
            current = current.next
            index += 1

        return number
    
class Solution:
    def sum(self, a: Node, b: Node) -> Node:
        sumNode: Node = Node(-1)
        temp = sumNode
        carry = 0
        while (a is not None or b is not None): 
            x = a.value if a is not None else 0
            y = b.value if b is not None else 0
            sum = x + y + carry
            carry = sum // 10
            number = sum % 10
            temp.next = Node(number)
            a = a.next if a != None else None
            b = b.next if b != None else None
            temp = temp.next

        if carry > 0:
            temp.next = Node(carry)

        return sumNode.next


linked1 = LinkedList()
linked1.push(Node(7))
linked1.push(Node(5))
linked1.push(Node(9))
print(linked1.show())
linked1.reverse()
print(linked1.show())

linked2 = LinkedList()
linked2.push(Node(9))
linked2.push(Node(8))
print(linked2.show())
linked2.reverse()
print(linked2.show())

s = Solution()
result: Node = s.sum(linked1.head, linked2.head)
final_linked_list = LinkedList()
final_linked_list.push(result)

print(final_linked_list.show())