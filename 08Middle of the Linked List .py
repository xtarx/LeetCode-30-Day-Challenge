import collections
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        len=1
        headOriginal=head
        while head.next != None:
            len+=1
            head=head.next;

        medianIndex=(int(float(len/2)))
        for i in range(medianIndex):
            headOriginal = headOriginal.next;
        print(headOriginal.val)
        return headOriginal



s1 = Solution();
inputArr=[1,2,3,4,5]
x=ListNode(inputArr[0])
x.next=ListNode(inputArr[1])
x.next.next=ListNode(inputArr[2])
x.next.next.next=ListNode(inputArr[3])
x.next.next.next.next=ListNode(inputArr[4])

#
# print(x.val)
# print(x.next.val)
print(s1.middleNode(x))
