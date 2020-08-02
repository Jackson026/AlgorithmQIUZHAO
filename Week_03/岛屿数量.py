
# grid 是二维矩阵
# 步骤：
# 1.遍历循环二维数组，遇见1时，把它周围相邻的1全部标为0（注意：标0）
# 2.递归运算，每个岛屿只留下一个1

def numIslands(self, grid) -> int:
    if not grid:
        return 0
    row, col = len(grid), len(grid[0])

    def mark(grid, r, c):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        mark(grid, r + 1, c)
        mark(grid, r - 1, c)
        mark(grid, r, c + 1)
        mark(grid, r, c - 1)

    res = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                mark(grid, r, c)
                res += 1
    return res