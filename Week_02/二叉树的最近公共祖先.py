
# 终止条件：
# 1.当越过叶节点，则直接返回null
# 2.当root等于p,q，直接返回root

# 递归工作
# 1.开启递归左子节点，返回值记为left
# 2.开启递归右子节点，返回值记为right

# 返回值：根据p,q，可能有四种情况
# 1.当left，right同时为空：说明root左右子树都不包含p,q，返回null
# 2.当left，right同时不为空：说明p,q同时root两侧，返回root
# 3.当left为空，right不为空：p,q都不在root的左子树，直接返回right。具体两种情况：
#    1.p,q其中一个在root右子树，此时right指向p
#    2.p,q两节点都在root右子树，此时right指向最近公共祖先节点
# 4.当left不为空，right为空，与3情况相反

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == q or root == p:
        return root
    root.left = self.lowestCommonAncestor(root.left, p, q)
    root.right = self.lowestCommonAncestor(root.right, p, q)
    if not root.left:
        return root.right
    if not root.right:
        return root.left
    return root