# 学习笔记

## 分治、回溯模版
def divide_conquer(problem, param1, param2, ...): <br/>
    #recursion terminator <br/>
    if problem is None: <br/>
         print_result <br/>
        return<br/>
    #prepare data <br/>
     data = prepare_data(problem) <br/>
     subproblems = split_problem(problem, data) <br/>
    #conquer subproblems <br/>
     subresult1 = self.divide_conquer(subproblems[0], p1, ...) <br/>
     subresult2 = self.divide_conquer(subproblems[1], p1, ...) <br/>
     subresult3 = self.divide_conquer(subproblems[2], p1, ...) <br/>
    ...<br/>
    #process and generate the final result <br/>
     result = process_result(subresult1, subresult2, subresult3, …) <br/>
    #revert the current level states<br/>
<br/>
<br/>
## DFS模版-递归写法
visited = set() <br/>
def dfs(node, visited): <br/>
    if node in visited: # terminator <br/>
        #already visited <br/>
        return <br/>
    visited.add(node) <br/>
    #process current node here. <br/>
    ...<br/>
    for next_node in node.children(): <br/>
        if not next_node in visited: <br/>
            dfs(next_node, visited)<br/>
<br/>
## DFS模版-非递归写法
def DFS(self, tree): <br/>
    if tree.root is None: <br/>
    return [] <br/>
    visited, stack = [], [tree.root] <br/>
    while stack: <br/>
        node = stack.pop() <br/>
        visited.add(node) <br/>
        process (node) <br/>
        nodes = generate_related_nodes(node) <br/>
        stack.push(nodes) <br/>
    #other processing work <br/>
    ...
<br/>
## BFS模版
def BFS(graph, start, end): <br/>
    queue = [] <br/>
    queue.append([start]) <br/>
    visited.add(start) <br/>
    while queue: <br/>
        node = queue.pop() <br/>
        visited.add(node) <br/>
        process(node) <br/>
        nodes = generate_related_nodes(node) <br/>
        queue.push(nodes) <br/>
    #other processing work <br/>
    ...
<br/>
## 贪心算法
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。<br/>
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。<br/>
简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。<br/>
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。<br/>
<br/>
## 二分查找
1. 目标函数单调性（单调递增或者递减）<br/>
2. 存在上下界（bounded）<br/>
3. 能够通过索引访问（index accessible)<br/>

#### 模版
left, right = 0, len(array) - 1<br/>
while left <= right:<br/>
    mid = (left + right) / 2<br/>
    if array[mid] == target: # find the target!! <br/>
        break or return result <br/>
    elif array[mid] < target:<br/>
        left = mid + 1<br/>
    else:<br/>
        right = mid - 1<br/>
