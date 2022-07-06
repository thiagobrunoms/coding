# Definition for singly-linked list.
from multiprocessing.dummy import current_process
from os import link


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = ListNode(head)

    def push(self, value):
        temp: ListNode = ListNode(value)
        temp.value = value
        temp.next = self.head
        self.head = temp

    def reverse_interactively(self):
        previous: ListNode = None
        current: ListNode = self.head
        next: ListNode = None

        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def reverse_recursively(self, head: ListNode):
        if head == None or head.next == None:
            return head

        reversed_node: ListNode = self.reverse_recursively(head.next)

        head.next.next = head
        head.next = None

        return reversed_node

    def show(self):
        current: ListNode = self.head

        while current != None:
            print(current.value)
            current = current.next

    # def reverse_iteractively(self):


linkedList = LinkedList(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)

# print('before reversing')
# linkedList.show()
# linkedList.reverse_interactively()
# print('after reversing')
# linkedList.show()

reversed_linked_list = linkedList.reverse_recursively(linkedList.head)

current: ListNode = reversed_linked_list
while current != None:
    print(current.value)
    current = current.next
