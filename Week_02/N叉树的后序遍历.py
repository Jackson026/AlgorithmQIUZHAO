
#  树的遍历模版

def postorder(self, root: 'Node'):
    res = []

    def helper(node):
        if node:

            for c in node.children:
                helper(c)
            res.append(node.val)

    helper(root)
    return res