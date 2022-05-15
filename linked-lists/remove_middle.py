# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
# Hints: #72

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

        self.middle_node = self.head
        self.current_index = 0

    def add(self, n: Node):
        self.current_index += 1

        if self.head.next == None:
            self.head.next = n
            return

        #1 -> 2 -> 3 ->
        currentNode = self.head
        count = 0
        while (currentNode.next != None):
            currentNode = currentNode.next
            count += 1

            if count == self.current_index // 2:
                self.middle_node = currentNode
                print("middle", self.middle_node)

        currentNode.next = n

    def get_n(self, n_element):
        current_node = self.head

        j = 0
        while(j < n_element or current_node == None):
            j = j + 1
            current_node = current_node.next

        return current_node

    def delete_middle(self):
        current_node = self.head
        previous_node = self.head

        while current_node != None:
            if current_node.node_id == self.middle_node.node_id:
                previous_node.next = current_node.next
                break
            else:
                previous_node = current_node
                current_node = current_node.next

        self.current_index -= 1

    def __str__(self):
        content = self.head.__str__()

        current_node = self.head.next
        while current_node != None:
            content += current_node.__str__()
            current_node = current_node.next

        return content

#1->2->3->4->5->6
linkedList = LinkedList(Node(1))
# print(linkedList)
linkedList.add(Node(2))
linkedList.add(Node(3))
linkedList.add(Node(4))
linkedList.add(Node(5))
linkedList.add(Node(6))
linkedList.add(Node(7))

print(linkedList)

linkedList.delete_middle()

print(linkedList)