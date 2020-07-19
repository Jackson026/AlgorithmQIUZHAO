def detectCycle(self, head):

    # 要找进入环的那个点，我们要做两件事
    # 第一是利用快慢指针找到第一次相遇的地方，根据推倒，此时改点到入环点的距离与头节点到入环点距离相同
    # 第二次两指针同时出发，一个从头节点，一个从相遇点，直到他们相遇时，找到入环点

    s,f=head,head
    while f and f.next:
        s=s.next
        f=f.next.next
        if s==f:
            s2=head
            while s2 is not s:
                s2=s2.next
                s=s.next
            return s
    else:
        return None


    # 利用set存储节点，因为其无重复性，所以在下一次遇到set内节点时，可判定该点为入环点

    s = set()
    while head:
        if head in s:
            return head
        else:
            s.add(head)
            head = head.next
    return None