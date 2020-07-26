class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
        return
    root = TreeNode(preorder[0])
    ind = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:1 + ind], inorder[:ind])
    root.right = self.buildTree(preorder[1 + ind:], inorder[ind + 1:])
    return root