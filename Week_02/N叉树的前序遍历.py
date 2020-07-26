
# 树的遍历 模版

def preorder(self, root: 'Node'):
    res = []

    def helper(node):
        if node:
            res.append(node.val)
            for c in node.children:
                helper(c)

    helper(root)
    return res