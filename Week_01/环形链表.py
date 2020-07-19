def hasCycle(self, head) -> bool:

    # 用set把节点存进去，while head，如果在set中就是环形，否则就不是

    s= set()
    while head:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False

    # 利用快慢指针，慢指针每次走一步，快指针每次两步
    # 循环head，如果快慢指针相遇为环，否则不是

    if not (head and head.next):
        return False
    i ,j =head, head.next
    while j and j.next:
        if i == j:
            return True
        i , j = i.next , j.next.next
    return False