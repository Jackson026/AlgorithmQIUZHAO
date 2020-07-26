# 第二周学习笔记
#### 排序类、组合类、树类的题目方法
#### 使用回溯算法完成

#### 类似这样的模版
#### 全排列类
1.无重复
def backtrack(nums, t):
    if not nums:
        res.append(t)
        return
    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i + 1:], t + [nums[i]])
backtrack(nums, [])

2.有重复
def helper(nums, t):
    if not nums:
        res.append(t)
        return
    visited = set()
    for i in range(len(nums)):
        if nums[i] in visited:
            continue
        helper(nums[:i] + nums[i + 1:], t + [nums[i]])
        visited.add(nums[i])
helper(nums, [])

#### 组合类
def backtrack(l, k, t):
    if k == 0:
        res.append(t)
        return
    for i in range(l, n + 1):
        backtrack(i + 1, k - 1, t + [i])
backtrack(1, k, [])

#### 树的遍历基本模版
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(self, root: TreeNode):
#1.用栈
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
    #
#2.用递归
    res=[]
    def helper(root):
        if root:                    #根据遍历的顺序，调整下面三句位置
            helper(root.left)
            res.append(root.val)
            helper(root.right)
    helper(root)
    return res


#### 层序遍历，可以用双端队列或者列表
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
        
        
#### 最近公共祖先问题，常考
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


注意：
题目需要反复练习，掌握每种类型题中的模版套路，死记硬背，并反复使用加强记忆，有助于对知识的理解
