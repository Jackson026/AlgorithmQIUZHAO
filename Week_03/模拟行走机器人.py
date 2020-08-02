
# 模拟 O(N+K)
# 我们将会存储机器人的位置和方向。如果机器人得到转弯的指令，我们就更新方向；否则就沿给定的方向走指定的步数。
# 必须注意使用 集合 Set 作为对障碍物使用的数据结构，以便我们可以有效地检查下一步是否受阻。如果不这样做，我们检查 该点是障碍点吗 可能会慢大约 10000 倍。
# 在某些语言中，我们需要将每个障碍物的坐标编码为 长整型 long 数据，以便它可以放入 集合 Set 数据结构中。或者，我们也可以将坐标编码为 字符串 string。

def robotSim(self, commands, obstacles):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    ans = 0

    for cmd in commands:
        if cmd == -2:  # left
            di = (di - 1) % 4
        elif cmd == -1:  # right
            di = (di + 1) % 4
        else:
            for k in range(cmd):
                if (x + dx[di], y + dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x * x + y * y)

    return ans
