# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
from pdb import line_prefix


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def add(self, n: ListNode):
        if self.head.next == None:
            self.head.next = n
            return

        currentNode = self.head
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = n

    def show(self):
        current: ListNode = self.head

        while (current != None):
            print(current.val)
            current = current.next


class Solution:
    def swapPairs(self, head: ListNode):
        if head == None or head.next == None:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(head.next.next)
        second.next = first

        return second


head = ListNode(0, None)
linkedList = LinkedList(head)
linkedList.add(ListNode(1))
linkedList.add(ListNode(2))
linkedList.add(ListNode(3))
linkedList.add(ListNode(4))
linkedList.show()

print('swapping')
s = Solution()
result = s.swapPairs(linkedList.head)
print('result')
linkedList = LinkedList(result)
linkedList.show()
