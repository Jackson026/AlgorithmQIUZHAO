# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(self, root: TreeNode):
    res = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            # res.append(cur.val)   #根据遍历的顺序，调整语句的位置
            stack.append(cur)
            cur = cur.right
        t = stack.pop()
        res.append(t.val)
        cur = t.left
    return res[::-1]

    res=[]
    def helper(root):
        if root:                    #根据遍历的顺序，调整下面三句位置
            helper(root.left)
            res.append(root.val)
            helper(root.right)
    helper(root)
    return res