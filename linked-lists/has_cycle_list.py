# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
# Output: C
# Hints: #50, #69, #83, #90

# A more convenient approach is to use a hashtable that keeps the nodes that were seen before. However, this requires an O(N) space
# Another more smart approach is to use the floyds algorithm. Both pointers will be equal if there is a cycle.

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

    def add(self, n: Node):
        if self.head.next == None:
            self.head.next = n
            return

        currentNode = self.head
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = n

    def has_cycle(self) -> bool:
        tortoise = self.head
        hare = self.head.next

        # need to test based on this condition: tortoise != None and tortoise.next != None and hare.fast != None???
        while (hare != None and hare.next != None):
            # if there is a cycle, both pointers will be the same at some part
            print("tortoise", tortoise.value, "hare", hare.value)
            if hare == tortoise:
                return True

            tortoise = tortoise.next
            hare = hare.next.next

        # hare gets None or hare.next gets None. Thus, no cycle found
        return False

    # def __str__(self):
    #     content = self.head.__str__()

    #     current_node = self.head.next
    #     while current_node != None:
    #         content += current_node.__str__()
    #         current_node = current_node.next

    #     return content


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

linked_list = LinkedList(n1)
linked_list.add(n2)
linked_list.add(n3)
linked_list.add(n4)
linked_list.add(n2)

# 1 -> 2 -> 3 -> 4 -> 2

print(linked_list)

has_cycle = linked_list.has_cycle()
print(has_cycle)
