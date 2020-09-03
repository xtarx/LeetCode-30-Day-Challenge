class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def printList(self, node):
        while node.next is not None:
            print(node.val)
            node = node.next
        print(node.val)


s = Solution();
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None
# s.printList(n1)
print(s.deleteNode(n2))
print('After Deletion')
s.printList(n1)
