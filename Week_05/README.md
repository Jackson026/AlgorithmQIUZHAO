学习笔记
## 双向BFS
1 给end和begin两个set，判断时两个queue都要判断<br/>
2 begin和end会按照长度互换，从长度短的set进行扩散<br/>
3 设置一下扩散点的集合 <br/>
4 遍历begin的set，遍历起始词的长度，遍历每一个字母a-z，替换掉beginword词的字母<br/>
5 如果new_word在end出现，说明相交，返回结果；否则扩散集合里加入它，词表中去除<br/>
6 把扩散集合赋给begin集合 <br/>

## A*搜索
class A*(Object):

    def AstarSearch(graph, start, end): 
         pq = collections.priority_queue() # 优先级 —> 估价函数
         pq.append([start]) 
         visited.add(start) 
             while pq: 
                 node = pq.pop() # can we add more intelligence here ? 
                 visited.add(node) 
                 process(node) 
                 nodes = generate_related_nodes(node) 
                 unvisited = [node for node in nodes if node not in visited] 
                 pq.push(unvisited)
估价函数：启发式函数： h(n)，它用来评价哪些结点最有希望的是一个我们要找的结
点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的估
计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测
哪个邻居结点会导向一个目标。
## Trie树
### Python 
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
		
### 基本结构
字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。
典型应用是用于统计和排序大量的字符串（但不仅限于字符串），
所以经常被搜索引擎系统用于文本词频统计。<br/>
优点：最大限度的减少无谓的字符串比较，查询效率比哈希表高.<br/>
### 基本性质
1.结点本身不存完整单词<br/>
2.从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串<br/>
3.每个结点的所有子结点路径代表的字符都不相同。<br/>
### 核心思想
空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。<br/>

## 并查集
### 基本操作
• makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。<br/>
• unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在
的集合不相交，如果相交则不合并。<br/>
• find(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元
素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。<br/>

class Disjoint(object):

    def init(p): 
        # for i = 0 .. n: p[i] = i; 
        p = [i for i in range(n)] 
    def union(self, p, i, j): 
        p1 = self.parent(p, i) 
        p2 = self.parent(p, j) 
        p[p1] = p2 
    def parent(self, p, i): 
        root = i 
        while p[root] != root: 
            root = p[root] 
        while p[i] != i: # 路径压缩 ? 
            x = i; i = p[i]; p[x] = root 
        return root
        
### 二叉树的遍历
class d_order(object):

    def preorder(self, root): 
        if root: 
            self.traverse_path.append(root.val) 
            self.preorder(root.left) 
            self.preorder(root.right)
    def inorder(self, root):
        if root: 
            self.inorder(root.left) 
            self.traverse_path.append(root.val) 
            self.inorder(root.right)
    def postorder(self, root):
        if root: 
            self.postorder(root.left) 
            self.postorder(root.right) 
            self.traverse_path.append(root.val)
            
### 二叉搜索树
二叉搜索树，也称二叉搜索树、有序二叉树（Ordered Binary Tree）、排
序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉树：
1. 左子树上所有结点的值均小于它的根结点的值；
2. 右子树上所有结点的值均大于它的根结点的值；
3. 以此类推：左、右子树也分别为二叉查找树。 （这就是 重复性！）

中序遍历：升序排列

## 平衡树
### AVL
1. 发明者 G. M. Adelson-Velsky和 Evgenii Landis
2. Balance Factor（平衡因子）：
是它的左子树的高度减去它的右子树的高度（有时相反）。
balance factor = {-1, 0, 1}
3. 通过旋转操作来进行平衡（四种）
4. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

旋转操作
1. 左旋
2. 右旋
3. 左右旋
4. 右左旋

### 红黑树
红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一
个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉
搜索树： <br/>
• 每个结点要么是红色，要么是黑色<br/>
• 根结点是黑色<br/>
• 每个叶结点（NIL结点，空结点）是黑色的。 <br/>
• 不能有相邻接的两个红色结点 <br/>
• 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。<br/>

关键性质：从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。<br/>
<br/>
对比：<br/>
• AVL trees providefaster lookups than Red Black Trees because they are more strictly 
balanced. <br/>
• Red Black Trees providefaster insertion and removal operations than AVL trees as 
fewer rotations are done due to relatively relaxed balancing.<br/>
• AVL trees storebalance factors or heightswith each node, thus requires storage for 
an integer per node whereas Red Black Tree requires only 1 bit of information per 
node.<br/>
• Red Black Trees are used in most of the language libraries 
likemap, multimap, multisetin C++whereas AVL trees are used indatabaseswhere 
faster retrievals are required.

## 位运算
指定位置的位运算
1. 将 x 最右边的 n 位清零：x & (~0 << n)
2. 获取 x 的第 n 位值（0 或者 1）： (x >> n) & 1
3. 获取 x 的第 n 位的幂值：x & (1 << n)
4. 仅将第 n 位置为 1：x | (1 << n)
5. 仅将第 n 位置为 0：x & (~ (1 << n))
6. 将 x 最高位至第 n 位（含）清零：x & ((1 << n) - 1)

实战位运算要点
1. 判断奇偶：<br/>
x % 2 == 1 —> (x & 1) == 1 <br/>
x % 2 == 0 —> (x & 1) == 0
2. x >> 1 —> x / 2 <br/>
即： x = x / 2; —> x = x >> 1<br/>
mid = (left + right) / 2 —> mid = (left + right) >> 1;
3.  X = X & (X-1) 清零最低位的 1 
4. X & -X => 得到最低位的 1 
5. X & ~X => 0

N皇后的位运算解法 - Python

class quees(object):

    def totalNQueens(self, n): 
        if n < 1: return [] 
        self.count = 0
        self.DFS(n, 0, 0, 0, 0) 
        return self.count
    def DFS(self, n, row, cols, pie, na): 
        # recursion terminator 
        if row >= n: 
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) — 1) # 得到当前所有的空位
        while bits: 
            p = bits & —bits # 取到最低位的1
            bits = bits & (bits — 1) # 表示在p位置上放入皇后
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) 
            # 不需要revert cols, pie, na 的状态