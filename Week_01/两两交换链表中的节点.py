# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # 递归方法，套路为  终止条件；本次递归所完成的事情；递归；处理

        if head is None or head.next is None:
            return head
        h=head.next
        head.next=self.swapPairs(head.next.next)
        h.next=head
        return h


        # 加了一个头节点，然后每次交换两个节点，最后将新加的头节点的这个位置转移到下一对节点之前

        pre,pre.next=self,head
        while pre.next and pre.next.next:
            a=pre.next
            b=a.next
            pre.next,a.next,b.next=b,b.next,a
            pre=a
        return self.next