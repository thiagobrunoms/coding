class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def push(self, value):
        current: ListNode = self.head

        while current.next != None:
            current = current.next

        temp = ListNode(value)
        temp.value = value

        current.next = ListNode(value)
        # temp: ListNode = ListNode(value)
        # temp.value = value
        # temp.next = self.head
        # self.head = temp

    def show(self):
        current: ListNode = self.head

        while current != None:
            print(current.val)
            current = current.next


class Solution:
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        if head1 == None:
            return head2

        if head2 == None:
            return head1

        if head1.val < head2.val:
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2


linkedList1 = LinkedList(ListNode(5))
linkedList1.push(10)
linkedList1.push(20)
linkedList1.push(30)
linkedList1.push(40)
linkedList1.push(50)
# linkedList1.show()

linkedList2 = LinkedList(ListNode(1))
linkedList2.push(15)
linkedList2.push(25)
linkedList2.push(35)
linkedList2.push(45)
linkedList2.push(55)

# linkedList2.show()

s = Solution()
merged = s.merge(linkedList1.head, linkedList2.head)

mergedLinkedList = LinkedList(merged)
mergedLinkedList.show()
