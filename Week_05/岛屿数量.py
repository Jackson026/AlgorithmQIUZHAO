class Solution:
    def numIslands(self, grid) -> int:
        # grid: List[List[str]]

        # 1.遍历循环二维数组，遇见1时，把它周围相邻的1全部标为0
        # 2.递归运算，每个岛屿只留下一个1

        if not grid or not grid[0]:
            return 0
        res = 0

        def dfsmark(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfsmark(grid, i + 1, j)
            dfsmark(grid, i - 1, j)
            dfsmark(grid, i, j + 1)
            dfsmark(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfsmark(grid, i, j)
                    res += 1
        return res

        # def union(p,i,j):
        #     p1=parent(p,i)
        #     p2=parent(p,j)
        #     p[p1]=p2
        # def parent(p,i):
        #     root=i
        #     while root!=p[root]:
        #         root=p[root]
        #     while i!=p[i]:
        #         x=i;i=p[i];p[x]=root
        #     return root
        # p=[i for i in range(len(grid))]
        # if not grid:return 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]=='1':
        #             for x, y in [[-1, 0], [0, -1], [1,0],[0,1]]:
        #                 tmp_i = i + x
        #                 tmp_j = j + y
        #                 if 0 <= tmp_i < len(grid) and 0 <= tmp_j < len(grid[0]) and grid[tmp_i][tmp_j] == "1":
        #                     union(p,i,j)

        # return len(set([parent(p,i) for i in range(len(grid))])) if grid[0][0]=='1' else 0