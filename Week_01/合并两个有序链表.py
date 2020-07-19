# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 使用的递归
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

# 方法2 设置一个头节点，然后依次加两个链表
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    prenode = ListNode(-1)
    pre = prenode
    while l1 and l2:
        if l1.val > l2.val:
            pre.next = l2
            l2 = l2.next
        else:
            pre.next = l1
            l1 = l1.next
        pre = pre.next
    pre.next = l1 if l1 is not None else l2
    return prenode.next
