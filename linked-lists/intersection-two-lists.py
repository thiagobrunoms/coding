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

    def addAtHead(self, val: int) -> None:
        current: Node = Node(val)
        current.next = self.head
        self.head = current
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
                return currentll1

            if currentll1 == None:
                currentll1 = ll2.head

            if currentll2 == None:
                currentll2 = ll1.head

        return currentll1


l1: MyLinkedList = MyLinkedList()
l1.addAtHead(10)
l1.addAtTail(20)
l1.addAtTail(30)
l1.addAtTail(40)
l1.addAtTail(50)
