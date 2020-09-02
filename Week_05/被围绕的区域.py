class Solution:
    def solve(self, board) -> None:
        # board: List[List[str]]
        """
        Do not return anything, modify board in-place instead.
        """
        # 并查集
        # f = {}
        # def find(x):
        #     f.setdefault(x, x)
        #     if f[x] != x:
        #         f[x] = find(f[x])
        #     return f[x]
        # def union(x, y):
        #     f[find(y)] = find(x)

        # if not board or not board[0]:
        #     return
        # row = len(board)
        # col = len(board[0])
        # dummy = row * col
        # for i in range(row):
        #     for j in range(col):
        #         if board[i][j] == "O":
        #             if i == 0 or i == row - 1 or j == 0 or j == col - 1:
        #                 union(i * col + j, dummy)
        #             else:
        #                 for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #                     if board[i + x][j + y] == "O":
        #                         union(i * col + j, (i + x) * col + (j + y))
        # for i in range(row):
        #     for j in range(col):
        #         if find(dummy) == find(i * col + j):
        #             board[i][j] = "O"
        #         else:
        #             board[i][j] = "X"


        # DFS and BFS
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        # dfs method
        def dfs(i, j):
            board[i][j] = 'B'
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tem_x = i + x
                tem_y = j + y
                if 1 <= tem_x < row and 1 <= tem_y < col and board[tem_x][tem_y] == 'O':
                    dfs(tem_x, tem_y)

        # bfs method
        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for i in range(col):
            if board[0][i] == 'O':
                bfs(0, i)
                # dfs(0,i)
            if board[row - 1][i] == 'O':
                bfs(row - 1, i)
                # dfs(row-1,i)
        for i in range(row):
            if board[i][0] == 'O':
                bfs(i, 0)
                # dfs(i,0)
            if board[i][col - 1] == 'O':
                bfs(i, col - 1)
                # dfs(i,col-1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'