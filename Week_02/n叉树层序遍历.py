class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        stack=[root]  #利用队列pop(0)或双端队列popleft()
        res=[]
        while stack:
            res.append([t.val for t in stack])
            stack=[c for t in stack for c in t.children]
        return res