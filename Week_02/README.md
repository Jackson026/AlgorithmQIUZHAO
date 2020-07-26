# 第二周学习笔记
#### 排序类、组合类、树类的题目方法
#### 使用回溯算法完成

#### 类似这样的模版
#### 全排列类
1.无重复<br/>
def backtrack(nums, t):<br/>
    if not nums:<br/>
        res.append(t)<br/>
        return<br/>
    for i in range(len(nums)):<br/>
        backtrack(nums[:i] + nums[i + 1:], t + [nums[i]])<br/>
backtrack(nums, [])<br/>
<br/>
<br/>
2.有重复<br/>
def helper(nums, t):<br/>
    if not nums:<br/>
        res.append(t)<br/>
        return<br/>
    visited = set()<br/>
    for i in range(len(nums)):<br/>
        if nums[i] in visited:<br/>
            continue<br/>
        helper(nums[:i] + nums[i + 1:], t + [nums[i]])<br/>
        visited.add(nums[i])<br/>
helper(nums, [])<br/>

#### 组合类
def backtrack(l, k, t):<br/>
    if k == 0:<br/>
        res.append(t)<br/>
        return<br/>
    for i in range(l, n + 1):<br/>
        backtrack(i + 1, k - 1, t + [i])<br/>
backtrack(1, k, [])<br/>

#### 树的遍历基本模版
class TreeNode:<br/>
    def __init__(self, x):<br/>
        self.val = x<br/>
        self.left = None<br/>
        self.right = None<br/>

def inorderTraversal(self, root: TreeNode):<br/>
#1.用栈<br/>
    res = []<br/>
    stack = []<br/>
    cur = root<br/>
    while stack or cur:<br/>
        while cur:<br/>
            # res.append(cur.val)   #根据遍历的顺序，调整语句的位置<br/>
            stack.append(cur)<br/>
            cur = cur.right<br/>
        t = stack.pop()<br/>
        res.append(t.val)<br/>
        cur = t.left<br/>
    return res[::-1]<br/>
    #<br/>
#2.用递归<br/>
    res=[]<br/>
    def helper(root):<br/>
        if root:                    #根据遍历的顺序，调整下面三句位置<br/>
            helper(root.left)<br/>
            res.append(root.val)<br/>
            helper(root.right)<br/>
    helper(root)<br/>
    return res<br/>
<br/>
<br/><br/>
#### 层序遍历，可以用双端队列或者列表
class Node:<br/>
    def __init__(self, val=None, children=None):<br/>
        self.val = val<br/>
        self.children = children<br/>
<br/>
class Solution:<br/>
    def levelOrder(self, root: 'Node'):<br/>
        if not root:<br/>
            return []<br/>
        stack=[root]  #利用队列pop(0)或双端队列popleft()<br/>
        res=[]<br/>
        while stack:<br/>
            res.append([t.val for t in stack])<br/>
            stack=[c for t in stack for c in t.children]<br/>
        return res<br/>
<br/>
<br/><br/>
#### 最近公共祖先问题，常考
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':<br/>
    if not root or root == q or root == p:<br/>
        return root<br/>
    root.left = self.lowestCommonAncestor(root.left, p, q)<br/>
    root.right = self.lowestCommonAncestor(root.right, p, q)<br/>
    if not root.left:<br/>
        return root.right<br/>
    if not root.right:<br/>
        return root.left<br/>
    return root<br/>
<br/>

注意：<br/>
题目需要反复练习，掌握每种类型题中的模版套路，死记硬背，并反复使用加强记忆，有助于对知识的理解
