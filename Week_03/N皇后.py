
# 1.构建全是'.'的棋盘
# 2.构建列、主对角线、副对角线
# 3.dfs遍历棋盘。 A：终止条件 B：当前层变为'Q' C:dfs递归 D：revert操作，还原一下

def solveNQueens(self, n: int):
    ans = []
    res = [['.'] * n for i in range(n)]
    col = [False] * 2 * n
    dg = [False] * 2 * n
    udg = [False] * 2 * n

    def dfs(u):
        lists = []
        if u == n:
            for i in range(n):
                lists.append(''.join(res[i]))
            ans.append(lists)
            return
        for i in range(n):
            if not col[i] and not dg[u + i] and not udg[n - u + i]:
                res[u][i] = 'Q'
                col[i] = dg[u + i] = udg[n - u + i] = True
                dfs(u + 1)
                res[u][i] = '.'
                col[i] = dg[u + i] = udg[n - u + i] = False

    dfs(0)
    return ans