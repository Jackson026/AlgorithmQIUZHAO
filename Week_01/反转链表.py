# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h_new=None
        while head:
            t=head.next
            head.next=h_new
            h_new=head
            head=t
        return h_new

# 将头节点指向空，然后依次改变后续节点指向，直到无head