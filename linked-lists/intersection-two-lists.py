from code import interact


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.head == None:
            return None

        if index > self.size or index < 0:
            return None

        if index == 0:
            return self.head

        count = 1
        current: Node = self.head.next
        while current != None:
            if index == count:
                return current

            current = current.next
            count += 1

    def addAtHead(self, node: Node) -> None:
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.size += 1
            return

        current: Node = self.head
        while current.next != None:
            current = current.next

        current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None

        if index == 0:
            self.addAtHead(val)
            return

        count = 0
        current: Node = self.head
        previous: Node = self.head
        while True:
            if count == index:
                new_node: Node = Node(val)
                previous.next = new_node
                new_node.next = current
                self.size += 1
                return

            count += 1
            previous = current
            current = current.next

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0 or index < 0 or index > self.size:
            return

        if index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next

            self.size -= 1
            return

        count = 0
        current: Node = self.head
        previous: Node = self.head
        while True:
            if count == index:
                previous.next = current.next
                self.size -= 1
                return

            count += 1
            previous = current
            current = current.next

    def show(self):
        current: Node = self.head
        while current != None:
            print(current.value)
            current = current.next


# class Intersection:
#     def intersect(self, ll1: LinkedList, ll2: LinkedList) -> str:
#         currentll1: Node = ll1.head
#         currentll2: Node = ll2.head

#         visited = set()
#         while currentll1 != None or currentll2 != None:
#             if (currentll1 != None and currentll1 in visited) or (currentll2 != None and currentll2 in visited):
#                 return 'Intersect in ', currentll1.value

#             visited.add(currentll1)
#             visited.add(currentll2)

#         return 'No intersection'

class Intersection:
    def intersect(self, ll1: MyLinkedList, ll2: MyLinkedList) -> Node:
        currentll1 = ll1.head
        currentll2 = ll2.head

        while currentll1 != currentll2:
            currentll1 = currentll1.next
            currentll2 = currentll2.next

            if currentll1 == currentll2:
                return currentll1  # No difference if returns currentll2?

            if currentll1 == None:
                currentll1 = ll2.head

            if currentll2 == None:
                currentll2 = ll1.head

        return currentll1  # No difference if returns currentll2?


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)

l1: MyLinkedList = MyLinkedList()
l1.addAtHead(n1)
l1.addAtHead(n2)
l1.addAtHead(n3)
l1.addAtHead(n4)
l1.addAtHead(n5)
l1.addAtHead(n6)
l1.addAtHead(n7)

n10 = Node(100)
n20 = Node(200)
n30 = Node(300)
n50 = Node(500)
n60 = Node(600)
n70 = Node(700)

l2: MyLinkedList = MyLinkedList()
l2.addAtHead(n10)
l2.addAtHead(n20)
l2.addAtHead(n30)
l2.addAtHead(n4)
l2.addAtHead(n50)

intersection = Intersection()
result = intersection.intersect(l1, l2)
print(result.value)
