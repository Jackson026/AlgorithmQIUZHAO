# 学习笔记

## 分治、回溯模版
class divid_conquer(object):

    def divide_conquer(problem, param1, param2, ...): 
        #recursion terminator 
        if problem is None: 
             print_result 
            return
        #prepare data 
         data = prepare_data(problem) 
         subproblems = split_problem(problem, data)
        #conquer subproblems 
         subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
         subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
         subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
        ...
        #process and generate the final result
         result = process_result(subresult1, subresult2, subresult3, …)
        #revert the current level states

## DFS模版-递归写法
class dfs_non_recrusion(object):

    visited = set() 
    def dfs(node, visited):
        if node in visited: # terminator 
            #already visited 
            return 
        visited.add(node)
        #process current node here
        ...
        for next_node in node.children(): 
            if not next_node in visited: 
                dfs(next_node, visited)
## DFS模版-非递归写法
class dfs_recrusion(object):

    def DFS(self, tree): 
        if tree.root is None: 
        return [] 
        visited, stack = [], [tree.root] 
        while stack:
            node = stack.pop()
            visited.add(node)
            process (node)
            nodes = generate_related_nodes(node)
            stack.push(nodes)
        #other processing work
        ...
## BFS模版
class bfs_recrusion(object):

    def BFS(graph, start, end): 
        queue = [] 
        queue.append([start]) 
        visited.add(start) 
        while queue: 
            node = queue.pop() 
            visited.add(node) 
            process(node)
            nodes = generate_related_nodes(node) 
            queue.push(nodes) 
        #other processing work 
        ...
## 贪心算法
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
<br/>
## 二分查找
1. 目标函数单调性（单调递增或者递减）
2. 存在上下界（bounded）
3. 能够通过索引访问（index accessible)
#### 模版
class divid_half(object):

    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target: # find the target!!
            break or return result 
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1